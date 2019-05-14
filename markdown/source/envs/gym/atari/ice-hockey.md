---
layout: page
title: Atari Ice Hockey Environment
permalink: /envs/gym/atari/ice-hockey/

redirect_from:
 - /envs/gym/atari-2600/ice-hockey/
 - /env/gym/atari/ice-hockey/
 - /env/gym/atari-2600/ice-hockey/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/ice-hockey.mp4' | absolute_url }}" type="video/mp4">
</video>

Ice Hockey is a game of two-on-two ice hockey. One player on each team is the goalie, and the other plays offensive (although, the goalie is not confined to the goal). As in the real sport, the object of the game is to take control of the puck and shoot it into the opposing goal to score points. When the puck is in player control, it moves left and right along the blade of the hockey stick. The puck can be shot at any of 32 angles, depending on the position of the puck when it's shot.

Human players take control of the skater in control of (or closest to) the puck. The puck can be stolen from its holder; shots can also be blocked by the blade of the hockey stick.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Ice_Hockey_%281981_video_game%29)*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
