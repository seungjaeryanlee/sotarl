---
layout: page
title: Atari River Raid Environment
permalink: /envs/gym/atari/riverraid/

redirect_from:
 - /envs/gym/atari-2600/river-raid/
 - /env/gym/atari/river-raid/
 - /env/gym/atari-2600/river-raid/
 - /envs/gym/atari/river-raid/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/riverraid.mp4' | absolute_url }}" type="video/mp4">
</video>

Viewed from a top-down perspective, the player flies a fighter jet over the River of No Return in a raid behind enemy lines. The player's jet can only move left and right—it cannot maneuver up and down the screen—but it can accelerate and decelerate. The player's jet crashes if it collides with the riverbank or an enemy craft, or if the jet runs out of fuel. Assuming fuel can be replenished, and if the player evades damage, gameplay is essentially unlimited.

The player scores points for shooting enemy tankers (30 pts), helicopters (60 pts), fuel depots (80 pts), jets (100 pts), and bridges (500 pts). The jet refuels when it flies over a fuel depot. A bridge marks the end of a game level. Non-Atari 2600 ports of the game add hot air balloons that are worth 60 points when shot as well as tanks along the sides of the river that shoot at the player's jet.

Destroying bridges also serve as the game's checkpoints. If the player crashes the plane they will start their next life at the last destroyed bridge.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/River_Raid)*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
