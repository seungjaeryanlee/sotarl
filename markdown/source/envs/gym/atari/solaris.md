---
layout: page
title: Atari Solaris Environment
permalink: /envs/gym/atari/solaris/

redirect_from:
 - /envs/gym/atari-2600/solaris/
 - /env/gym/atari/solaris/
 - /env/gym/atari-2600/solaris/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/solaris.mp4' | absolute_url }}" type="video/mp4">
</video>

The galaxy of Solaris is made up of 16 quadrants, each containing 48 sectors. The player uses a tactical map to choose a sector to warp to, during which they must attempt to keep their ship "in focus" to lower their fuel consumption rate. Fuel must be carefully managed, as an empty tank results in loss of one of the player lives. Space battle ensues whenever the player navigates into a hostile battlegroup via the tactical map. Space enemies include pirate ships, mechanoid ships, and aggressive "cobra" ships. Each battlegroup has at least one enemy flagship, which shoots out fuel-sapping drones.

The player may also descend to one of 3 types of planets.

1. Friendly federation planets, which provide for refueling, but may also harbor a planet defense mission if they are under attack. If players allow a friendly planet in a quadrant to be destroyed, that quadrant becomes a "red zone" where joystick controls are reversed and booming sounds are overheard.
2. Enemy Zylon planets, in which the player must rescue all cadets, gaining an extra ship when all cadets are rescued.
3. Enemy corridor planets, in which the player must traverse through a fast-paced corridor.

There are 4 kinds of ground enemies found on planets: stationary guardians, gliders, targeters and raiders. The ultimate goal of Solaris is to reach the planet Solaris and rescue its colonists, at which point the game ends in victory.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Solaris_(video_game))*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
