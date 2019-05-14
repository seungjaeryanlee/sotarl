---
layout: page
title: Atari Pong Environment
permalink: /envs/gym/atari/pong/

redirect_from:
 - /envs/gym/atari-2600/pong/
 - /env/gym/atari/pong/
 - /env/gym/atari-2600/pong/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/pong.mp4' | absolute_url }}" type="video/mp4">
</video>

Pong is a two-dimensional sports game that simulates table tennis. The player controls an in-game paddle by moving it vertically across the left or right side of the screen. They can compete against another player controlling a second paddle on the opposing side. Players use the paddles to hit a ball back and forth. The goal is for each player to reach eleven points before the opponent; points are earned when one fails to return the ball to the other.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Pong)*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
