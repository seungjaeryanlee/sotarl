---
layout: page
title: Atari Surround Environment
permalink: /envs/gym/atari/surround/

redirect_from:
 - /envs/gym/atari-2600/surround/
 - /env/gym/atari/surround/
 - /env/gym/atari-2600/surround/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/surround.mp4' | absolute_url }}" type="video/mp4">
</video>

Like its predecessor Blockade, the object of Surround is to maneuver a square across the screen, leaving a trail behind. A player wins by forcing the other player to crash into one of the trails. Twelve game variations include options allow for speed-up, diagonal movement, wrap-around, and "erase" (the choice to not draw at a given moment). In addition, the sprites can be set to operate at a slower speed, or progressively speed up through five speeds.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Surround_(video_game))*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
