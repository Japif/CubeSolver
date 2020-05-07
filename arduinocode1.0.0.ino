#include "Stepper.h"

const int PASSI = 360;
const int VELOCITA = 20;

String string = "";
char mosse[200];
char mossa;
int inv = 0, passiU, passiL, passiB, passiR, passiF, passiD,
    esci = 0, totale = 0, rotX = 0, rotY = 0, rotZ=0;
int pinU[] = {1, 2};
int pinL[] = {3, 4};
int pinB[] = {5, 6};
int pinR[] = {7, 8};
int pinD[] = {9, 10};
int pinF[] = {11, 12};

Stepper serU(PASSI, pinU[0], pinU[1]);
Stepper serL(PASSI, pinL[0], pinL[1]);
Stepper serB(PASSI, pinB[0], pinB[1]);
Stepper serR(PASSI, pinR[0], pinR[1]);
Stepper serD(PASSI, pinD[0], pinD[1]);
Stepper serF(PASSI, pinF[0], pinF[1]);


void setup() {
  serU.setSpeed(VELOCITA);
  serL.setSpeed(VELOCITA);
  serB.setSpeed(VELOCITA);
  serR.setSpeed(VELOCITA);
  serF.setSpeed(VELOCITA);
  serD.setSpeed(VELOCITA);
  Serial.begin(19200);
}

void loop() {
  //Fai fino alla risoluzione
  while (esci == 0) {
    //carattere in input
    char character;
    //Prendi i dati, passa in carattere e poi aggiungi a string. Conta.
     while (!Serial.available()) {}
      while (Serial.available())
     {
      character = Serial.read();
      string.concat(character);
      totale++;
      delay(10);
     }
     //Porta tutto ad array
     string.toCharArray(mosse, 200);
     delay(200);
     //OPZ 
     Serial.println(mosse);
  //Leggi un comando completo alla volta
    for (int i = 0; i <= totale; i++) {
      if (mosse[i] == ' ')
        i++;
      if (mosse[i] == 'O') {
        esci = 1;
        break;
      }
      mossa = mosse[i];
      if (mosse[i + 1] == 'i')
        inv = 1;
      i++;
      /*
        /////////////////////////////////////////////////////////CONTROLLO
        Serial.print("mossa è:");
        Serial.println(mossa);
        Serial.print("i è:");
        Serial.println(i);
        Serial.print("Invertito? ");
        Serial.println(inv);
      */

      switch (mossa) {
        case 'U':
          if (rotX == 0 && rotZ == 0)
            passiU = PASSI / 4;
          else if (rotX == 1 && rotZ == 0)
            passiF = PASSI / 4;
          else if (rotX == 2 && rotZ == 0)
            passiD = PASSI / 4;
          else if (rotX == 3 && rotZ == 0)
            passiB = PASSI / 4;
          if (rotZ == 0 && rotX == 0)
            passiU = PASSI / 4;
          else if (rotZ == 1 && rotX == 0)
            passiL = PASSI / 4;
          else if (rotZ == 2 && rotX == 0)
            passiD = PASSI / 4;
          else if (rotZ == 3 && rotX == 0)
            passiR = PASSI / 4;
          break;

        case 'L':
          if (rotY == 0 && rotZ == 0)
            passiL = PASSI / 4;
          else if (rotY == 1 && rotZ == 0)
            passiF = PASSI / 4;
          else if (rotY == 2 && rotZ == 0)
            passiR = PASSI / 4;
          else if (rotY == 3  && rotZ == 0)
            passiB = PASSI / 4;
          if (rotZ == 0 && rotY == 0)
            passiL = PASSI / 4;
          else if (rotZ == 1 && rotY == 0)
            passiD = PASSI / 4;
          else if (rotZ == 2 && rotY == 0)
            passiR = PASSI / 4;
          else if (rotZ == 3  && rotY == 0)
            passiU = PASSI / 4;
          break;

        case 'B':
          if (rotX == 0  && rotY == 0)
            passiB = PASSI / 4;
          else if (rotX == 1 && rotY == 0)
            passiU = PASSI / 4;
          else if (rotX == 2 && rotY == 0)
            passiF = PASSI / 4;
          else if (rotX == 3 && rotY == 0)
            passiD = PASSI / 4;
          if (rotY == 0 && rotX == 0)
            passiB = PASSI / 4;
          else if (rotY == 1 && rotX == 0)
            passiL = PASSI / 4;
          else if (rotY == 2 && rotX == 0)
            passiF = PASSI / 4;
          else if (rotY == 3  && rotX == 0)
            passiR = PASSI / 4;
          break;

        case 'R':
          if (rotY == 0 && rotZ == 0)
            passiR = PASSI / 4;
          else if (rotY == 1 && rotZ == 0)
            passiB = PASSI / 4;
          else if (rotY == 2 && rotZ == 0)
            passiL = PASSI / 4;
          else if (rotY == 3 && rotZ == 0)
            passiF = PASSI / 4;
          if (rotZ == 0 && rotY == 0)
            passiR = PASSI / 4;
          else if (rotZ == 1 && rotY == 0)
            passiU = PASSI / 4;
          else if (rotZ == 2 && rotY == 0)
            passiL = PASSI / 4;
          else if (rotZ == 3 && rotY == 0)
            passiD = PASSI / 4;
          break;

        case 'F':
          if (rotX == 0  && rotY == 0)
            passiF = PASSI / 4;
          else if (rotX == 1  && rotY == 0)
            passiD = PASSI / 4;
          else if (rotX == 2  && rotY == 0)
            passiB = PASSI / 4;
          else if (rotX == 3   && rotY == 0)
            passiU = PASSI / 4;
          if (rotY == 0  && rotX == 0)
            passiF = PASSI / 4;
          else if (rotY == 1  && rotX == 0)
            passiR = PASSI / 4;
          else if (rotY == 2  && rotX == 0)
            passiB = PASSI / 4;
          else if (rotY == 3  && rotX == 0)
            passiL = PASSI / 4;
          break;

        case 'D':
          if (rotX == 0  && rotZ == 0)
            passiD = PASSI / 4;
          else if (rotX == 1  && rotZ == 0)
            passiB = PASSI / 4;
          else if (rotX == 2  && rotZ == 0)
            passiU = PASSI / 4;
          else if (rotX == 3  && rotZ == 0)
            passiF = PASSI / 4;
          if (rotZ == 0  && rotX == 0)
            passiD = PASSI / 4;
          else if (rotZ == 1  && rotX == 0)
            passiR = PASSI / 4;
          else if (rotZ == 2  && rotX == 0)
            passiU = PASSI / 4;
          else if (rotZ == 3  && rotX == 0)
            passiL = PASSI / 4;
          break;

        /////////////////////////ROTAZIONI
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

        case 'O': //O di ornitorinco
          esci = 1;
          break;
      }
      if (inv == 1) {
        passiU = 0 - passiU;
        passiL = 0 - passiL;
        passiB = 0 - passiB;
        passiR = 0 - passiR;
        passiF = 0 - passiF;
        passiD = 0 - passiD;
        inv = 0;
      }
      if (passiU != 0) {
        serU.step(passiU);
        Serial.print("muovo U di ");
        Serial.println(passiU);
      }
      if (passiL != 0) {
        serL.step(passiL);
        Serial.print("muovo L di ");
        Serial.println(passiL);
      }
      if (passiB != 0) {
        serB.step(passiB);
        Serial.print("muovo B di ");
        Serial.println(passiB);
      }
      if (passiR != 0) {
        serR.step(passiR);
        Serial.print("muovo R di ");
        Serial.println(passiR);
      }
      if (passiF != 0) {
        serF.step(passiF);
        Serial.print("muovo F di ");
        Serial.println(passiF);
      }
      if (passiD != 0) {
        serD.step(passiD);
        Serial.print("muovo D di ");
        Serial.println(passiD);
      }
      passiU = 0;
      passiL = 0;
      passiB = 0;
      passiR = 0;
      passiF = 0;
      passiD = 0;
      inv = 0;
    }
  }
  Serial.print("FINEH");
  exit(0);
}
