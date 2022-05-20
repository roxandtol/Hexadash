![Hexadash](Repo-Pictures/Hexadash.png)

# A free and Open Source Rhythm game

## The basics:

Hexadash is a game where you're a hexagon, and you need to move between 3 slots and press a button to the beat. 

There are two kinds of notes:
1) Single:
You simply have to press the button when the note comes 
1) Hold: 
You press the button when the note starts and release it when it  ends

You always need to be in the same slot. when pressing beats, and there's a combo counter that will change your score

--- 

## Performance:

Depending on the precision of your press, you may get:
- 300 points (Perfect)
- 100 points
- 50 points
- No points (You didn't press / Too early or too late)

Each note will add 1 to the Combo counter.

The equation that the game follows to get the value of a press is:

```
Value = (Press Value * combo) / 10
```
And at the end of the beatmap, you will get your numerical score + a letter, each letter will have a different meaning:

- SS: All beats have been 300
- S: No missed beats
- A: There has been a single miss
- B: Less than 15% of the beats were missed
- C: Less than 25% of the beats were missed
- D: More than 25% of the beats were missed

If you fail more than 5% of the beats in a row, the beatmap will end early

---
## Maps: 
Every single beat will be 150 ms-

The structure of a beatmap beat file is:
```
{slot},{Beat lenght},{Delay till next beat}
```
And every map will be stored on a folder, and inside the folder, you'll find: 
- Beat file (.HD)
- Song (.mp3, .wav or .ogg)
- Beatsound (.mp3, .wav or .ogg)