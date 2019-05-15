---
layout: page
title: Atari Environments
permalink: /envs/gym/atari/
redirect_from:
 - /envs/gym/atari-2600
 - /env/gym/atari
 - /env/gym/atari-2600
 - /envs/atari

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
 - name: Installation
   permalink: '#installation'
 - name: Variants
   permalink: '#variants'

---

<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--3-col mdl-cell--3-col-desktop mdl-cell--4-col-tablet  mdl-cell--12-col-phone">
    <video autoplay muted loop controls>
      <source src="{{ 'assets/_pages/envs/gym/atari/beam-rider.mp4' | absolute_url }}" type="video/mp4">
    </video>
  </div>
  <div class="mdl-cell mdl-cell--3-col mdl-cell--3-col-desktop mdl-cell--4-col-tablet  mdl-cell--12-col-phone mdl-cell--hide-phone">
    <video autoplay muted loop controls>
      <source src="{{ 'assets/_pages/envs/gym/atari/breakout.mp4' | absolute_url }}" type="video/mp4">
    </video>
  </div>
  <div class="mdl-cell mdl-cell--3-col mdl-cell--3-col-desktop mdl-cell--4-col-tablet  mdl-cell--12-col-phone mdl-cell--hide-phone mdl-cell--hide-tablet">
    <video autoplay muted loop controls>
      <source src="{{ 'assets/_pages/envs/gym/atari/montezumas-revenge.mp4' | absolute_url }}" type="video/mp4">
    </video>
  </div>
  <div class="mdl-cell mdl-cell--3-col mdl-cell--3-col-desktop mdl-cell--4-col-tablet  mdl-cell--12-col-phone mdl-cell--hide-phone mdl-cell--hide-tablet">
    <video autoplay muted loop controls>
      <source src="{{ 'assets/_pages/envs/gym/atari/qbert.mp4' | absolute_url }}" type="video/mp4">
    </video>
  </div>
</div>

## Overview

Atari 2600 is a video game console from Atari that was released in 1977. The game console included popular games such as *Breakout*, *Ms. Pacman* and *Space Invaders*. Since Deep Q-Networks were introduced by Mnih et al. in 2013, Atari 2600 has been the standard environment to test new Reinforcement Learning algorithms. Atari 2600 has been a challenging testbed due to its high-dimensional video input (size 210 x 160, frequency 60 Hz) and the discrepancy of tasks between games.

The Atari 2600 environments was originally provided through the [Arcade Learning Environment (ALE)](https://github.com/mgbellemare/Arcade-Learning-Environment). The environments have been wrapped by OpenAI Gym to create a more standardized interface. The OpenAI Gym provides 59 Atari 2600 games as environments.



## State of the Art

*Note: Most papers use 57 Atari 2600 games, and a couple of them are not supported by OpenAI Gym.*

These are the published state-of-the-art results for Atari 2600 testbed. To test the robustness of the agent, most papers use one or both settings: the *no-op starts* and the *human starts*, both devised to provide a nondeterministic starting position. In *No-op start* setting, the agent selects the "do nothing" action for up to 30 times at the start of an episode. providing random starting positions to the agent. This originates from the [DQN2015 paper](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf) by Mnih et al. (2015). In the *human start* setting,  the agents start from one of the 100 starting points sampled from a human professional's gameplay. The human starts setting originates from the [GorilaDQN paper](https://arxiv.org/abs/1507.04296) by Nair et al. (2015).

### Median

One popular method of checking the agent's overall performance is the *median human-normalized score*. You can read more about the choice of this metric in the [Rainbow paper](https://arxiv.org/abs/1710.02298). For better comparison of algorithms,  we only used results that were tested on majority of the games available.

#### No-op starts

| Median | Method                | Score from                                                   |
| ------ | --------------------- | ------------------------------------------------------------ |
| 434%   | Ape-X DQN<sup>1</sup> | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 331%   | UNREAL<sup>2</sup>    | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 223%   | Rainbow DQN           | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| 178%   | C51                   | [A Distributional Perspective on Reinforcement Learning](https://arxiv.org/abs/1707.06887) |
| 172%   | NoisyNet-Dueling DDQN | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| 164%   | Distributional DQN    | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| 151%   | Dueling DDQN          | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 140%   | Prioritized DDQN      | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 132%   | Dueling DDQN          | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| 123%   | NoisyNet-DQN          | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| 118%   | NoisyNet-DQN          | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| 117%   | DDQN                  | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 96%    | Gorila DQN            | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 83%    | DQN<sup>3</sup>       | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| 80%    | A3C                   | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| 79%    | DQN<sup>3</sup>       | [A Distributional Perspective on Reinforcement Learning](https://arxiv.org/abs/1707.06887) |

<sub>
<sup>1</sup> Ape-X DQN used a lot more (x100) environment frames compared to other results. The training time is half the time of other DQN results.<br/>
<sup>2</sup> Hyperparameters were tuned per game.<br/>
<sup>3</sup> Only evaluated on 49 games.
</sub>

#### Human starts

| Median | Method                | Score from                                                   |
| ------ | --------------------- | ------------------------------------------------------------ |
| 358%   | Ape-X DQN<sup>1</sup> | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 250%   | UNREAL<sup>2</sup>    | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 153%   | Rainbow DQN           | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| 128%   | Prioritized DDQN      | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 125%   | C51                   | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 125%   | Distributional DQN    | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| 117%   | Dueling DDQN          | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 116%   | A3C                   | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 110%   | DDQN                  | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| 102%   | Noisy DQN             | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| 78%    | Gorila DQN            | [Distributed Prioritized Experience Replay]( https://arxiv.org/abs/1803.00933) |
| 68%    | DQN<sup>3</sup>       | [Rainbow: Combining Improvements in Deep Reinforcement Learning]( https://arxiv.org/abs/1710.02298) |

<sub>
<sup>1</sup> Ape-X DQN used a lot more (x100) environment frames compared to other results. The training time is half the time of other DQN results.<br/>
<sup>2</sup> Hyperparameters were tuned per game. <br/>
<sup>3</sup> Only evaluated on 49 games.
</sub>

### Individual Environments

Although the metric above is a valuable way of comparing the general effectiveness of an algorithm, different algorithms have different strengths. Thus, we also included the state-of-the-art results for each game.

If you want to see how other methods performed in each Atari 2600 games, you can check the results of all methods by clicking the name of the game in the table below.

#### No-op Starts

| Game                                                      | Result      | Method              | Type      | Score from                                                   |
| --------------------------------------------------------- | ----------- | ------------------- | --------- | ------------------------------------------------------------ |
| [Alien](/envs/gym/atari/alien)                            | 40804.9     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Amidar](/envs/gym/atari/amidar)                          | 8659.2      | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Assault](/envs/gym/atari/assault)                        | 24559.4     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Asterix](/envs/gym/atari/asterix)                        | 428200.3    | RainbowDQN          | DQN       | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| [Asteroids](/envs/gym/atari/asteroids)                    | 155495.1    | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Atlantis](/envs/gym/atari/atlantis)                      | 3433182.0   | ACKTR               | PG        | [Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation](https://arxiv.org/abs/1708.05144) |
| [Bank Heist](/envs/gym/atari/bank-heist)                  | 1716.4      | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Battle Zone](/envs/gym/atari/battle-zone)                | 98895.0     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Beam Rider](/envs/gym/atari/beam-rider)                  | 63305.2     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [**Bowling**](/envs/gym/atari/bowling)                    | **160.7**   | **Human**           | **Human** | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| [Boxing](/envs/gym/atari/boxing)                          | 100.0       | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Breakout](/envs/gym/atari/breakout)                      | 800.9       | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Centipede](/envs/gym/atari/centipede)                    | 49065.8     | DDQN+PopArt         | DQN       | [Learning values across many orders of magnitude](https://arxiv.org/abs/1602.07714) |
| [Chopper Command](/envs/gym/atari/chopper-command)        | 721851.0    | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Crazy Climber](/envs/gym/atari/crazy-climber)            | 320426.0    | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Demon Attack](/envs/gym/atari/demon-attack)              | 274176.7    | ACKTR               | PG        | [Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation](https://arxiv.org/abs/1708.05144) |
| [Double Dunk](/envs/gym/atari/double-dunk)                | 23.5        | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Enduro](/envs/gym/atari/enduro)                          | 3454.0      | C51                 | Misc      | [A Distributional Perspective on Reinforcement Learning](https://arxiv.org/abs/1707.06887) |
| [Fishing Derby](/envs/gym/atari/fishing-derby)            | 57.0        | NoisyNet-DuelingDQN | DQN       | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| [Freeway](/envs/gym/atari/freeway)                        | 34.0        | RainbowDQN          | DQN       | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| [Frostbite](/envs/gym/atari/frostbite)                    | 9590.5      | RainbowDQN          | DQN       | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| [Gopher](/envs/gym/atari/gopher)                          | 120500.9    | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [**Gravitar**](/envs/gym/atari/gravitar)                  | **3351.4**  | **Human**           | **Human** | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| [H.E.R.O.](/envs/gym/atari/hero)                          | 105929.4    | DQfD                | Imitation | [Deep Q-Learning from Demonstrations](https://arxiv.org/abs/1704.03732) |
| [Ice Hockey](/envs/gym/atari/ice-hockey)                  | 33.0        | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [James Bond](/envs/gym/atari/james-bond)                  | 21322.5     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Kangaroo](/envs/gym/atari/kangaroo)                      | 16200.0     | PERDDQN (rank)      | DQN       | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| [Krull](/envs/gym/atari/krull)                            | 22849.0     | NoisyNet-A3C        | PG        | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| [Kung-Fu Master](/envs/gym/atari/kung-fu-master)          | 97829.5     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Montezuma's Revenge](/envs/gym/atari/montezumas-revenge) | 41098.4     | YouTube             | Imitation | [Playing hard exploration games by watching YouTube](https://arxiv.org/abs/1805.11592) |
| [**Ms. Pacman**](/envs/gym/atari/ms-pacman)               | **15693**   | **Human**           | **Human** | [Human-level control through deep reinforcement learning](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf) |
| [Name This Game](/envs/gym/atari/name-this-game)          | 25783.3     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Pong](/envs/gym/atari/pong)                              | 21.0        | DDQN                | DQN       | [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461) |
| [Private Eye](/envs/gym/atari/private-eye)                | 98763.2     | YouTube             | Imitation | [Playing hard exploration games by watching YouTube](https://arxiv.org/abs/1805.11592) |
| [Q*Bert](/envs/gym/atari/qbert)                           | 302391.3    | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [River Raid](/envs/gym/atari/river-raid)                  | 63864.4     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Road Runner](/envs/gym/atari/road-runner)                | 234352.0    | NoisyNet-DuelingDQN | DQN       | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| [Robotank](/envs/gym/atari/robotank)                      | 73.8        | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Seaquest](/envs/gym/atari/seaquest)                      | 392952.3    | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Space Invaders](/envs/gym/atari/space-invaders)          | 54681.0     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Star Gunner](/envs/gym/atari/star-gunner)                | 434342.5    | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Tennis](/envs/gym/atari/tennis)                          | 23.9        | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Time Pilot](/envs/gym/atari/time-pilot)                  | 87085.0     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Tutankham](/envs/gym/atari/tutankham)                    | 314.3       | ACKTR               | PG        | [Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation](https://arxiv.org/abs/1708.05144) |
| [Up and Down](/envs/gym/atari/up-and-down)                | 436665.8    | ACKTR               | PG        | [Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation](https://arxiv.org/abs/1708.05144) |
| [Venture](/envs/gym/atari/venture)                        | 1813.0      | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Video Pinball](/envs/gym/atari/video-pinball)            | 949604.0    | C51                 | Misc      | [A Distributional Perspective on Reinforcement Learning](https://arxiv.org/abs/1707.06887) |
| [Wizard of Wor](/envs/gym/atari/wizard-of-wor)            | 46204.0     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Zaxxon](/envs/gym/atari/zaxxon)                          | 42285.5     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Berzerk](/envs/gym/atari/berzerk)                        | 57196.7     | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Defender](/envs/gym/atari/defender)                      | 411943.5    | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Phoenix](/envs/gym/atari/phoenix)                        | 224491.1    | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Pit Fall](/envs/gym/atari/pit-fall)                      | 60258.9     | YouTube             | Imitation | [Playing hard exploration games by watching YouTube](https://arxiv.org/abs/1805.11592) |
| [**Skiing**](/envs/gym/atari/skiing)                      | **-4336.9** | **Human**           | **Human** | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| [Solaris](/envs/gym/atari/solaris)                        | 12380.0     | A3C                 | PG        | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| [Surround](/envs/gym/atari/surround)                      | 10.0        | NoisyNet-DuelingDQN | DQN       | [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295) |
| [Yars Revenge](/envs/gym/atari/yars-revenge)              | 148594.8    | ApeX DQN            | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |

#### Human Starts

| Game                                                         | Result      | Method            | Type      | Score from                                                   |
| ------------------------------------------------------------ | ----------- | ----------------- | --------- | ------------------------------------------------------------ |
| [Alien](/envs/gym/atari/alien)                               | 17731.5     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [**Amidar**](/envs/gym/atari/amidar)                         | **1540.4**  | **Human**         | **Human** | [Massively Parallel Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1507.04296) |
| [Assault](/envs/gym/atari/assault)                           | 24404.6     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Asterix](/envs/gym/atari/asterix)                           | 395599.5    | DistributionalDQN | DQN       | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| [Asteroids](/envs/gym/atari/asteroids)                       | 117303.4    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Atlantis](/envs/gym/atari/atlantis)                         | 918714.5    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Bank Heist](/envs/gym/atari/bank-heist)                     | 1200.8      | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Battle Zone](/envs/gym/atari/battle-zone)                   | 92275.0     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Beam Rider](/envs/gym/atari/beam-rider)                     | 72233.7     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [**Bowling**](/envs/gym/atari/bowling)                       | **146.5**   | **Human**         | **Human** | [Massively Parallel Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1507.04296) |
| [Boxing](/envs/gym/atari/boxing)                             | 80.9        | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Breakout](/envs/gym/atari/breakout)                         | 766.8       | A3C LSTM          | PG        | [Asynchronous Methods for Deep Learning](https://arxiv.org/abs/1602.01783) |
| [**Centipede**](/envs/gym/atari/centipede)                   | **10321.9** | **Human**         | **Human** | [Massively Parallel Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1507.04296) |
| [Chopper Command](/envs/gym/atari/chopper-command)           | 576601.5    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Crazy Climber](/envs/gym/atari/crazy-climber)               | 263953.5    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Demon Attack](/envs/gym/atari/demon-attack)                 | 133002.1    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Double Dunk](/envs/gym/atari/double-dunk)                   | 22.3        | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Enduro](/envs/gym/atari/enduro)                             | 2223.9      | DuelingPERDQN     | DQN       | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| [Fishing Derby](/envs/gym/atari/fishing-derby)               | 22.6        | RainbowDQN        | DQN       | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| [Freeway](/envs/gym/atari/freeway)                           | 29.1        | RainbowDQN        | DQN       | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| [Frostbite](/envs/gym/atari/frostbite)                       | 6511.5      | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Gopher](/envs/gym/atari/gopher)                             | 121168.2    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [**Gravitar**](/envs/gym/atari/gravitar)                     | **3116.0**  | **Human**         | **Human** | [Massively Parallel Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1507.04296) |
| [H.E.R.O.](/envs/gym/atari/hero)                             | 50496.8     | RainbowDQN        | DQN       | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| [Ice Hockey](/envs/gym/atari/ice-hockey)                     | 24.0        | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [James Bond](/envs/gym/atari/james-bond)                     | 18992.3     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Kangaroo](/envs/gym/atari/kangaroo)                         | 12185.0     | PERDDQN (rank)    | DQN       | [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) |
| [Krull](/envs/gym/atari/krull)                               | 11209.5     | PERDQN (rank)     | DQN       | [Prioritized Experience Replay](https://arxiv.org/abs/1511.05952) |
| [Kung-Fu Master](/envs/gym/atari/kung-fu-master)             | 72068.0     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [**Montezuma's Revenge**](/envs/gym/atari/montezumas-revenge) | **4182.0**  | **Human**         | **Human** | [Massively Parallel Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1507.04296) |
| [**Ms. Pacman**](/envs/gym/atari/ms-pacman)                  | **15375.0** | **Human**         | **Human** | [Massively Parallel Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1507.04296) |
| [Name This Game](/envs/gym/atari/name-this-game)             | 23829.9     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Pong](/envs/gym/atari/pong)                                 | 19.1        | DDQN              | DQN       | [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461) |
| [**Private Eye**](/envs/gym/atari/private-eye)               | **64169.1** | **Human**         | **Human** | [Massively Parallel Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1507.04296) |
| [Q*Bert](/envs/gym/atari/qbert)                              | 380152.1    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [River Raid](/envs/gym/atari/river-raid)                     | 49982.8     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Road Runner](/envs/gym/atari/road-runner)                   | 127111.5    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Robotank](/envs/gym/atari/robotank)                         | 68.5        | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Seaquest](/envs/gym/atari/seaquest)                         | 377179.8    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Space Invaders](/envs/gym/atari/space-invaders)             | 50699.3     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Star Gunner](/envs/gym/atari/star-gunner)                   | 432958.0    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Tennis](/envs/gym/atari/tennis)                             | 23.0        | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Time Pilot](/envs/gym/atari/time-pilot)                     | 71543.0     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Tutankham](/envs/gym/atari/tutankham)                       | 156.3       | A3C FF (4 days)   | PG        | [Asynchronous Methods for Deep Learning](https://arxiv.org/abs/1602.01783) |
| [Up and Down](/envs/gym/atari/up-and-down)                   | 347912.2    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [**Venture**](/envs/gym/atari/venture)                       | **1039.0**  | **Human**         | **Human** | [Massively Parallel Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1507.04296) |
| [Video Pinball](/envs/gym/atari/video-pinball)               | 873988.5    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Wizard of Wor](/envs/gym/atari/wizard-of-wor)               | 46897.0     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Zaxxon](/envs/gym/atari/zaxxon)                             | 37672.0     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Berzerk](/envs/gym/atari/berzerk)                           | 55598.9     | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Defender](/envs/gym/atari/defender)                         | 399865.3    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [Phoenix](/envs/gym/atari/phoenix)                           | 188788.5    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |
| [**Pit Fall**](/envs/gym/atari/pit-fall)                     | **5998.9**  | **Human**         | **Human** | [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461) |
| [**Skiing**](/envs/gym/atari/skiing)                         | **-3686.6** | **Human**         | **Human** | [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461) |
| [**Solaris**](/envs/gym/atari/solaris)                       | **11032.6** | **Human**         | **Human** | [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461) |
| [Surround](/envs/gym/atari/surround)                         | 7.0         | RainbowDQN        | DQN       | [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) |
| [Yars Revenge](/envs/gym/atari/yars-revenge)                 | 131701.1    | ApeX DQN          | DQN       | [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) |





## Installation

### Prerequisites

To install the Atari 2600 environment, you need the OpenAI Gym toolkit. Read [this page](/envs/gym) to learn how to install OpenAI Gym.

### Installation via pip

If you did a full install of OpenAI Gym, the Atari 2600 should already be installed. Otherwise, you can install the Atari 2600 environment with a single `pip` command:

```bash
pip3 install gym[atari]
```

### Test Installation

You can run a simple random agent to make sure the Atari 2600 environment was correctly installed.

```python
import gym
env = gym.make('Pong-v0')
done = False
while not done:
    _, _, done, _ = env.step(env.action_space.sample())
    env.render()
env.close()
```



## Variants

In OpenAI Gym, each game has a few variants, distinguished by their suffixes. Through these variants, you can configure frame skipping and sticky actions. Frame skipping is a technique of using $k$-th frame. In other words, the agent only makes action every $k$ frames, and the same action is performed for $k$ frames. Sticky actions is a technique of setting some nonzero probability $p$ of action being repeated without agent's control. This adds  stochasticity to the deterministic Atari 2600 environments.

For example, there are six variants for the *Pong* environment.

| Name                                | Frame Skip $k$  | Repeat action probability $p$ |
| ----------------------------------- | --------------- | ----------------------------- |
| `Pong-v0`                           | 2~4<sup>1</sup> | 0.25                          |
| `Pong-v4`                           | 2~4<sup>1</sup> | 0                             |
| `PongDeterministic-v0`              | 4 <sup>2</sup>  | 0.25                          |
| `PongDeterministic-v4` <sup>3</sup> | 4 <sup>2</sup>  | 0                             |
| `PongNoFrameskip-v0`                | 1               | 0.25                          |
| `PongNoFrameskip-v4`                | 1               | 0                             |

<sub>
<sup>1</sup> $k$ is chosen randomly at every step from values $\{2, 3, 4\}$.<br/><sup>2</sup> For *Space Invaders*,  the `Deterministic` variant $k=3$. This is because when $k=4$, the lasers are invisible because it frame skip coincides with the blinking frequency of lasers.<br/><sup>3</sup> `Deterministic-v4` is the configuration used to assess Deep Q-Networks.
</sub>

For more details about *frame skipping* and *sticky actions*, check Sections 2 and 5 of the ALE whitepaper: [Revisiting the Arcade Learning Environment](https://arxiv.org/abs/1709.06009).

Also, there are RAM environments such as `Pong-ram-v0`, where the observation is the RAM of the Atari machine instead of the 210 x 160 visual input. You can also add suffixes to RAM environments.

