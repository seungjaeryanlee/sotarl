---
layout: page
title: Atari Bowling Environment
permalink: /envs/gym/atari/bowling/

redirect_from:
 - /envs/gym/atari-2600/bowling/
 - /env/gym/atari/bowling/
 - /env/gym/atari-2600/bowling/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/bowling.mp4' | absolute_url }}" type="video/mp4">
</video>

The game is based on the game of bowling, playable by one player or two players alternating.

In all six variations, games last for 10 frames, or turns. At the start of each frame, the current player is given two chances to roll a bowling ball down an alley in an attempt to knock down as many of the ten bowling pins as possible. The bowler (on the left side of the screen) may move up and down his end of the alley to aim before releasing the ball. In four of the game's six variations, the ball can be steered before it hits the pins. Knocking down every pin on the first shot is a strike, while knocking every pin down in both shots is a spare. The player's score is determined by the number of pins knocked down in all 10 frames, as well as the number of strikes and spares acquired.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Bowling_%28video_game%29)*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
