import copy
from dataclasses import dataclass, field
import heapq
import sys

MM_COST = 53
MM_DAMAGE = 4

DRAIN_COST = 73
DRAIN_EFFECT = 2

SHIELD_COST = 113
SHIELD_DURATION = 6
SHIELD_EFFECT = 7

POISON_COST = 173
POISON_DURATION = 6
POISON_EFFECT = 3

RECHARGE_COST = 229
RECHARGE_DURATION = 5
RECHARGE_EFFECT = 101


@dataclass(order=True)
class Fighter:
    hit_points: int
    damage: int = 0
    armor: int = 0
    mana: int = 0


@dataclass(order=True)
class GameState:
    mana_spent: int
    player: Fighter
    boss: Fighter
    shield_timer: int = 0
    poison_timer: int = 0
    recharge_timer: int = 0
    player_turn: bool = True
    spells_cast: list = field(default_factory=list)


player = Fighter(hit_points=50, mana=500)
boss = Fighter(*list(map(int, sys.argv[1:3])))

hard_mode = False
if len(sys.argv) > 3 and sys.argv[3] == "--hard":
    hard_mode = True


q = []

lowest_mana_spent = float("inf")
winning_state = None

heapq.heappush(q, GameState(0, player, boss))

while q:
    state = heapq.heappop(q)

    if state.mana_spent > lowest_mana_spent:
        continue
    state = copy.deepcopy(state)

    if state.poison_timer > 0:
        state.poison_timer -= 1
        state.boss.hit_points -= POISON_EFFECT
        if state.boss.hit_points <= 0:
            if state.mana_spent < lowest_mana_spent:
                lowest_mana_spent = state.mana_spent
                winning_state = state
            continue

    if state.shield_timer > 0:
        state.shield_timer -= 1
        state.player.armor = SHIELD_EFFECT
    else:
        state.player.armor = 0

    if state.recharge_timer > 0:
        state.recharge_timer -= 1
        state.player.mana += RECHARGE_EFFECT

    if state.player_turn:
        state.player_turn = False
        if hard_mode:
            state.player.hit_points -= 1
            if state.player.hit_points <= 0:
                continue

        if state.player.mana >= MM_COST:
            # cast Magic Missile
            new_state = copy.deepcopy(state)
            new_state.spells_cast.append("Magic Missile")
            new_state.mana_spent += MM_COST
            new_state.player.mana -= MM_COST
            new_state.boss.hit_points -= MM_DAMAGE
            if new_state.boss.hit_points <= 0:
                if new_state.mana_spent < lowest_mana_spent:
                    lowest_mana_spent = new_state.mana_spent
                    winning_state = new_state
                continue
            heapq.heappush(q, new_state)
        if state.player.mana >= DRAIN_COST:
            # cast Drain
            new_state = copy.deepcopy(state)
            new_state.spells_cast.append("Drain")
            new_state.mana_spent += DRAIN_COST
            new_state.player.mana -= DRAIN_COST
            new_state.boss.hit_points -= DRAIN_EFFECT
            new_state.player.hit_points += DRAIN_EFFECT
            if new_state.boss.hit_points <= 0:
                if new_state.mana_spent < lowest_mana_spent:
                    lowest_mana_spent = new_state.mana_spent
                    winning_state = new_state
                continue
            heapq.heappush(q, new_state)
        if state.shield_timer == 0 and state.player.mana >= SHIELD_COST:
            # cast Shield
            new_state = copy.deepcopy(state)
            new_state.spells_cast.append("Shield")
            new_state.mana_spent += SHIELD_COST
            new_state.player.mana -= SHIELD_COST
            new_state.shield_timer = SHIELD_DURATION
            heapq.heappush(q, new_state)
        if state.poison_timer == 0 and state.player.mana >= POISON_COST:
            # cast Poison
            new_state = copy.deepcopy(state)
            new_state.spells_cast.append("Poison")
            new_state.mana_spent += POISON_COST
            new_state.player.mana -= POISON_COST
            new_state.poison_timer = POISON_DURATION
            heapq.heappush(q, new_state)
        if state.recharge_timer == 0 and state.player.mana >= RECHARGE_COST:
            # cast Recharge
            new_state = copy.deepcopy(state)
            new_state.spells_cast.append("Recharge")
            new_state.mana_spent += RECHARGE_COST
            new_state.player.mana -= RECHARGE_COST
            new_state.recharge_timer = RECHARGE_DURATION
            heapq.heappush(q, new_state)
    else:  # boss turn
        state.player_turn = True
        damage = max(1, state.boss.damage - state.player.armor)
        state.player.hit_points -= damage
        if state.player.hit_points > 0:
            heapq.heappush(q, state)

print(winning_state)
