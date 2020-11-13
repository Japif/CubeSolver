//SET STEPS Per Revolution (200 by default) and RPM
const int STEPSPR = 200;
const int SPEED = 20;

//Motor pins {dir, step}
int pinU[] = {1, 2};
int pinL[] = {3, 4};
int pinB[] = {5, 6};
int pinR[] = {7, 8};
int pinD[] = {9, 10};
int pinF[] = {11, 12};

int ics = 300000 / SPEED;
/*
  X rpm = X*STEPSPR steps each minute = X steps/60000000 per microsecond
  200X/60000000 = X/300000 steps per microseconds
  RPM:300000 = 1 step:X
  X=300000/RPM
*/

String string = "";
char moves[200];
char move;
int inv = 0, stepsU, stepsL, stepsB, stepsR, stepsF, stepsD,
    endIt = 0, totale = 0, rotX = 0, rotY = 0, rotZ = 0;

void doSteps(int steps, int mot[])
{
    if (steps < 0)
    {
        steps = 0 - steps;
        digitalWrite(mot[0], LOW);
    }
    else
    {
        digitalWrite(mot[0], HIGH);
    }
    for (int i = 0; i < steps; i++)
    {
        digitalWrite(mot[1], HIGH);
        delayMicroseconds(ics);
        digitalWrite(mot[1], LOW);
        delayMicroseconds(ics);
    }
}

void setup()
{
    Serial.begin(19200);
}

void loop()
{
    //Keep doing until solved
    while (endIt == 0)
    {
        //input char
        char character;
        //Take data, put it into character, then add to string. Count.
        while (!Serial.available())
        {
        }
        while (Serial.available())
        {
            character = Serial.read();
            string.concat(character);
            totale++;
            delay(10);
        }
        //Put to array
        string.toCharArray(moves, 200);
        delay(200);
        //OPTIONAL
        Serial.println(moves);
        //Read a complete command a time
        for (int i = 0; i <= totale; i++)
        {
            if (moves[i] == ' ')
                i++;
            if (moves[i] == 'O')
            {
                endIt = 1;
                break;
            }
            move = moves[i];
            if (moves[i + 1] == 'i')
                inv = 1;
            i++;
            /*
        /////////////////////////////////////////////////////////CONTROL
        Serial.print("move is:");
        Serial.println(move);
        Serial.print("i is:");
        Serial.println(i);
        Serial.print("Invert? ");
        Serial.println(inv);
      */

            switch (move)
            {
            case 'U':
                if (rotX == 0 && rotZ == 0)
                    stepsU = STEPSPR / 4;
                else if (rotX == 1 && rotZ == 0)
                    stepsF = STEPSPR / 4;
                else if (rotX == 2 && rotZ == 0)
                    stepsD = STEPSPR / 4;
                else if (rotX == 3 && rotZ == 0)
                    stepsB = STEPSPR / 4;
                if (rotZ == 0 && rotX == 0)
                    stepsU = STEPSPR / 4;
                else if (rotZ == 1 && rotX == 0)
                    stepsL = STEPSPR / 4;
                else if (rotZ == 2 && rotX == 0)
                    stepsD = STEPSPR / 4;
                else if (rotZ == 3 && rotX == 0)
                    stepsR = STEPSPR / 4;
                break;

            case 'L':
                if (rotY == 0 && rotZ == 0)
                    stepsL = STEPSPR / 4;
                else if (rotY == 1 && rotZ == 0)
                    stepsF = STEPSPR / 4;
                else if (rotY == 2 && rotZ == 0)
                    stepsR = STEPSPR / 4;
                else if (rotY == 3 && rotZ == 0)
                    stepsB = STEPSPR / 4;
                if (rotZ == 0 && rotY == 0)
                    stepsL = STEPSPR / 4;
                else if (rotZ == 1 && rotY == 0)
                    stepsD = STEPSPR / 4;
                else if (rotZ == 2 && rotY == 0)
                    stepsR = STEPSPR / 4;
                else if (rotZ == 3 && rotY == 0)
                    stepsU = STEPSPR / 4;
                break;

            case 'B':
                if (rotX == 0 && rotY == 0)
                    stepsB = STEPSPR / 4;
                else if (rotX == 1 && rotY == 0)
                    stepsU = STEPSPR / 4;
                else if (rotX == 2 && rotY == 0)
                    stepsF = STEPSPR / 4;
                else if (rotX == 3 && rotY == 0)
                    stepsD = STEPSPR / 4;
                if (rotY == 0 && rotX == 0)
                    stepsB = STEPSPR / 4;
                else if (rotY == 1 && rotX == 0)
                    stepsL = STEPSPR / 4;
                else if (rotY == 2 && rotX == 0)
                    stepsF = STEPSPR / 4;
                else if (rotY == 3 && rotX == 0)
                    stepsR = STEPSPR / 4;
                break;

            case 'R':
                if (rotY == 0 && rotZ == 0)
                    stepsR = STEPSPR / 4;
                else if (rotY == 1 && rotZ == 0)
                    stepsB = STEPSPR / 4;
                else if (rotY == 2 && rotZ == 0)
                    stepsL = STEPSPR / 4;
                else if (rotY == 3 && rotZ == 0)
                    stepsF = STEPSPR / 4;
                if (rotZ == 0 && rotY == 0)
                    stepsR = STEPSPR / 4;
                else if (rotZ == 1 && rotY == 0)
                    stepsU = STEPSPR / 4;
                else if (rotZ == 2 && rotY == 0)
                    stepsL = STEPSPR / 4;
                else if (rotZ == 3 && rotY == 0)
                    stepsD = STEPSPR / 4;
                break;

            case 'F':
                if (rotX == 0 && rotY == 0)
                    stepsF = STEPSPR / 4;
                else if (rotX == 1 && rotY == 0)
                    stepsD = STEPSPR / 4;
                else if (rotX == 2 && rotY == 0)
                    stepsB = STEPSPR / 4;
                else if (rotX == 3 && rotY == 0)
                    stepsU = STEPSPR / 4;
                if (rotY == 0 && rotX == 0)
                    stepsF = STEPSPR / 4;
                else if (rotY == 1 && rotX == 0)
                    stepsR = STEPSPR / 4;
                else if (rotY == 2 && rotX == 0)
                    stepsB = STEPSPR / 4;
                else if (rotY == 3 && rotX == 0)
                    stepsL = STEPSPR / 4;
                break;

            case 'D':
                if (rotX == 0 && rotZ == 0)
                    stepsD = STEPSPR / 4;
                else if (rotX == 1 && rotZ == 0)
                    stepsB = STEPSPR / 4;
                else if (rotX == 2 && rotZ == 0)
                    stepsU = STEPSPR / 4;
                else if (rotX == 3 && rotZ == 0)
                    stepsF = STEPSPR / 4;
                if (rotZ == 0 && rotX == 0)
                    stepsD = STEPSPR / 4;
                else if (rotZ == 1 && rotX == 0)
                    stepsR = STEPSPR / 4;
                else if (rotZ == 2 && rotX == 0)
                    stepsU = STEPSPR / 4;
                else if (rotZ == 3 && rotX == 0)
                    stepsL = STEPSPR / 4;
                break;

            /////////////////////////ROTATIONS
            case 'X':
                rotX++;
                if (rotX == 4)
                    rotX = 0;
                break;

            case 'Y':
                rotY++;
                if (rotY == 4)
                    rotY = 0;
                break;

            case 'Z':
                rotZ++;
                if (rotZ == 4)
                    rotZ = 0;
                break;

            case 'H':
                rotX--;
                if (rotX < 0)
                    rotX = 3;
                break;

            case 'I':
                rotY--;
                if (rotY < 0)
                    rotY = 3;
                break;

            case 'J':
                rotZ--;
                if (rotZ < 0)
                    rotZ = 3;
                break;

            case 'O': //O of steps: ornitorinco
                endIt = 1;
                break;
            }
            if (inv == 1)
            {
                stepsU = 0 - stepsU;
                stepsL = 0 - stepsL;
                stepsB = 0 - stepsB;
                stepsR = 0 - stepsR;
                stepsF = 0 - stepsF;
                stepsD = 0 - stepsD;
                inv = 0;
            }
            if (stepsU != 0)
            {
                doSteps(stepsU, pinU);
                Serial.print("I move U of steps: ");
                Serial.println(stepsU);
            }
            if (stepsL != 0)
            {
                doSteps(stepsL, pinL);
                Serial.print("I move L of steps: ");
                Serial.println(stepsL);
            }
            if (stepsB != 0)
            {
                doSteps(stepsB, pinB);
                Serial.print("I move B of steps: ");
                Serial.println(stepsB);
            }
            if (stepsR != 0)
            {
                doSteps(stepsR, pinR);
                Serial.print("I move R of steps: ");
                Serial.println(stepsR);
            }
            if (stepsF != 0)
            {
                doSteps(stepsF, pinF);
                Serial.print("I move F of steps: ");
                Serial.println(stepsF);
            }
            if (stepsD != 0)
            {
                doSteps(stepsD, pinD);
                Serial.print("I move D of steps: ");
                Serial.println(stepsD);
            }
            stepsU = 0;
            stepsL = 0;
            stepsB = 0;
            stepsR = 0;
            stepsF = 0;
            stepsD = 0;
            inv = 0;
        }
    }
    Serial.print("END");
    exit(0);
}
