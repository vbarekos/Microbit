input.onButtonPressed(Button.A, function () {
    guess += -1
    basic.showNumber(guess)
})
input.onButtonPressed(Button.B, function () {
    guess += 1
    basic.showNumber(guess)
})
input.onGesture(Gesture.Shake, function () {
    if (guess == secret) {
        basic.showIcon(IconNames.Happy)
        basic.pause(2000)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.InBackground)
        basic.clearScreen()
    } else if (guess < secret) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            . . # . .
            . . # . .
            `)
        basic.pause(2000)
        basic.clearScreen()
    } else {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . # # # .
            . . # . .
            `)
        basic.pause(2000)
        basic.clearScreen()
    }
})
let secret = 0
let guess = 0
guess = 5
secret = randint(1, 10)
basic.showString("GUESS NUMBER")
music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
basic.showNumber(guess)
