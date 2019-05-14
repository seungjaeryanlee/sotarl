---
layout: page
title: Atari Time Pilot Environment
permalink: /envs/gym/atari/time-pilot/

redirect_from:
 - /envs/gym/atari-2600/time-pilot/
 - /env/gym/atari/time-pilot/
 - /env/gym/atari-2600/time-pilot/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/time-pilot.mp4' | absolute_url }}" type="video/mp4">
</video>

The player assumes the role of a pilot of a futuristic fighter jet, trying to rescue fellow pilots trapped in different time eras. In each level the player must fight off hordes of enemy craft then defeat a much stronger enemy ship. The player's plane always remains in the center of the screen.

The player travels through five time periods, rescuing stranded fellow pilots. The player must fight off droves of enemy craft while picking up parachuting friendly pilots. Once 56 enemy craft are defeated, initially 25 on the MSX platform and increasing by 5 after each game cycle (finishing the last battle against the UFOs), the player must defeat the mothership for the time period. Once she is destroyed, any remaining enemy craft are also eliminated and the player time-travels to the next level. All the levels have a blue sky and clouds as the background except the last level, which has space and asteroids instead. The specific eras visited, the common enemies, and the motherships are the following:

1. 1910: biplanes and a blimp
2. 1940: WWII monoplanes and a B-25
3. 1970: helicopters and a large, blue CH-46
4. 1982 (Konami version)/1983 (Centuri version): jets and a B-52
5. 2001: UFOs

The mothership is destroyed with seven direct hits. Once all the eras have been visited, the levels start over again but are harder and faster. The Game Boy Advance version of Time Pilot in Konami Arcade Classics includes a hidden sixth era, 1,000,000 BC, where the player must destroy vicious pterodactyls in order to return to the early 20th century.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Time_Pilot)*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
