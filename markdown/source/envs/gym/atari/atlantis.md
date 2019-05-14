---
layout: page
title: Atari Atlantis Environment
permalink: /envs/gym/atari/atlantis/

redirect_from:
 - /envs/gym/atari-2600/atlantis/
 - /env/gym/atari/atlantis/
 - /env/gym/atari-2600/atlantis/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/atlantis.mp4' | absolute_url }}" type="video/mp4">
</video>

The player controls the last defenses of the City of Atlantis against the Gorgon invaders. The city has seven bases, which are vulnerable to attack. Three of these have firepower capabilities to destroy the Gorgon ships before they manage to fire death rays at one of the settlements. The gun bases have fixed cannons; the center base fires straight up, while the far left and far right bases fire diagonally upwards across the screen. The center cannon also creates a shield that protects the settlements from the death rays, so once the center cannon is destroyed, the remaining settlements become vulnerable to attack. The enemy ships pass back and forth from left to right four times before they enter firing range, giving an ample opportunity to blow them away. Lost bases can be regained by destroying enough Gorgon ships.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Atlantis_%28video_game%29)*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
