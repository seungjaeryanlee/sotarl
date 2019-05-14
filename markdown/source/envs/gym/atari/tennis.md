---
layout: page
title: Atari Tennis Environment
permalink: /envs/gym/atari/tennis/

redirect_from:
 - /envs/gym/atari-2600/tennis/
 - /env/gym/atari/tennis/
 - /env/gym/atari-2600/tennis/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/tennis.mp4' | absolute_url }}" type="video/mp4">
</video>

Tennis offers singles matches for one or two players; one player is colored pink, the other blue. The game has two user-selectable speed levels. When serving and returning shots, the tennis players automatically swing forehand or backhand as the situation demands, and all shots automatically clear the net and land in bounds.

The first player to win one six-game set is declared the winner of the match (if the set ends in a 6-6 tie, the set restarts from 0-0). This differs from professional tennis, in which player must win at least two out of three six-game sets.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Tennis_(1981_video_game))*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
