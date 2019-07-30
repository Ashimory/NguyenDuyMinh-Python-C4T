from pyglet.media import Source, Player, load
player = Player()
source = load('4Qf_EPcgbSs.mp3')
player.queue(source)
player.play()
while True:
  playback = int(input('Press 1 to pause, 2 to stop'))
  if playback == 1:
    player.pause()
    playback_paused = int(input('Press 1 to resume, 2 to stop'))
    if playback_paused == 1:
      player.play()
    elif playback_paused == 2:
      break
  if playback == 2:
    break