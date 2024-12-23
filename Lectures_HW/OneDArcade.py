import asyncio


class Monster:
    def __init__(self, name, position, delay, strength):
        self.name = name
        self.position = position
        self.delay = delay
        self.strength = strength
        self.alive = True
        self.current_epoch = 0

    async def run(self, start_barrier, end_barrier):
        try:
            while True:
                await start_barrier.wait()
                if self.alive:
                    self.current_epoch += 1
                    if self.current_epoch % self.delay == 0:
                        self.position += 1
                await end_barrier.wait()
        except asyncio.CancelledError:
            pass


async def game(monsters, start_barrier, end_barrier, epochs):
    death_count=0
    for epoch in range(1, epochs + 1):
        if len(monsters) - death_count == 1:
            break
        await start_barrier.wait()
        await asyncio.sleep(0)

        await end_barrier.wait()

        alive_monsters = [m for m in monsters if m.alive]
        position_map = {}
        for monster in alive_monsters:
            pos = monster.position
            if pos in position_map:
                opponent = position_map[pos]
                if opponent.alive and monster.alive:
                    if monster.strength == opponent.strength:
                        monster.alive = False
                        opponent.alive = False
                        death_count+=2
                    elif monster.strength > opponent.strength:
                        monster.strength -= opponent.strength
                        opponent.alive = False
                        death_count+=1
                    else:
                        opponent.strength -= monster.strength
                        monster.alive = False
                        death_count+=1
                    break
            else:
                position_map[pos] = monster
        if all(not m.alive for m in monsters):
            return "All dead"
    if all(m.alive for m in monsters):
        return "All flee"
    else:
        survivors = [m.name for m in monsters if m.alive]
        return ", ".join(survivors)