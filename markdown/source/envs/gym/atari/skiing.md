---
layout: page
title: Atari Skiing Environment
permalink: /envs/gym/atari/skiing/

redirect_from:
 - /envs/gym/atari-2600/skiing/
 - /env/gym/atari/skiing/
 - /env/gym/atari-2600/skiing/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/skiing.mp4' | absolute_url }}" type="video/mp4">
</video>

Skiing is a single player only game, in which the player uses the joystick to control the direction and speed of a stationary skier at the top of the screen, while the background graphics scroll upwards, thus giving the illusion the skier is moving. The player must avoid obstacles, such as trees and moguls. The game cartridge contains five variations each of two principal games.

In the downhill mode, the player's goal is to reach the bottom of the ski course as rapidly as possible, while a timer records his relative success.

In the slalom mode, the player must similarly reach the end of the course as rapidly as he can, but must at the same time pass through a series of gates (indicated by a pair of closely spaced flagpoles). Each gate missed counts as a penalty against the player's time.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Skiing_%28Atari_2600%29)*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
