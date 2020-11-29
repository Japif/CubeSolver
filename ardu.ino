//IMPOSTA passi ogni giro (200) e RPM
const int PASSI = 200;
const int VELOCITA = 20;

//Motori {dir, step}
int pinU[] = {1, 2};
int pinL[] = {3, 4};
int pinB[] = {5, 6};
int pinR[] = {7, 8};
int pinD[] = {9, 10};
int pinF[] = {11, 12};

int ics = 300000 / VELOCITA;
/*
  X rpm = X*PASSI passi ogni min = X Passi/60000000 ogni microsecondi
  200X/60000000 = X/300000 passi ogni microsecondo
  RPM:300000=1 passo:X
  X=300000/RPM
*/
String string = "";
char mosse[200];
char mossa;
int inv = 0, passiU, passiL, passiB, passiR, passiF, passiD,
    esci = 0, totale = 0, rotX = 0, rotY = 0, rotZ = 0;

void faiStep(int, int []);

void setup() {
  Serial.begin(19200);
}

void loop() {
  //Fai fino alla risoluzione
  while (esci == 0) {
    //carattere in input
    char character;
    //Prendi i dati, passa in carattere e poi aggiungi a string. Conta.
    while (!Serial.available()) {}
    while (Serial.available()) {
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
          else if (rotY == 3 && rotZ == 0)
            passiB = PASSI / 4;
          if (rotZ == 0 && rotY == 0)
            passiL = PASSI / 4;
          else if (rotZ == 1 && rotY == 0)
            passiD = PASSI / 4;
          else if (rotZ == 2 && rotY == 0)
            passiR = PASSI / 4;
          else if (rotZ == 3 && rotY == 0)
            passiU = PASSI / 4;
          break;

        case 'B':
          if (rotX == 0 && rotY == 0)
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
          else if (rotY == 3 && rotX == 0)
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
          if (rotX == 0 && rotY == 0)
            passiF = PASSI / 4;
          else if (rotX == 1 && rotY == 0)
            passiD = PASSI / 4;
          else if (rotX == 2 && rotY == 0)
            passiB = PASSI / 4;
          else if (rotX == 3 && rotY == 0)
            passiU = PASSI / 4;
          if (rotY == 0 && rotX == 0)
            passiF = PASSI / 4;
          else if (rotY == 1 && rotX == 0)
            passiR = PASSI / 4;
          else if (rotY == 2 && rotX == 0)
            passiB = PASSI / 4;
          else if (rotY == 3 && rotX == 0)
            passiL = PASSI / 4;
          break;

        case 'D':
          if (rotX == 0 && rotZ == 0)
            passiD = PASSI / 4;
          else if (rotX == 1 && rotZ == 0)
            passiB = PASSI / 4;
          else if (rotX == 2 && rotZ == 0)
            passiU = PASSI / 4;
          else if (rotX == 3 && rotZ == 0)
            passiF = PASSI / 4;
          if (rotZ == 0 && rotX == 0)
            passiD = PASSI / 4;
          else if (rotZ == 1 && rotX == 0)
            passiR = PASSI / 4;
          else if (rotZ == 2 && rotX == 0)
            passiU = PASSI / 4;
          else if (rotZ == 3 && rotX == 0)
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
        faiStep(passiU, pinU);
        Serial.print("muovo U di ");
        Serial.println(passiU);
      }
      if (passiL != 0) {
        faiStep(passiL, pinL);
        Serial.print("muovo L di ");
        Serial.println(passiL);
      }
      if (passiB != 0) {
        faiStep(passiB, pinB);
        Serial.print("muovo B di ");
        Serial.println(passiB);
      }
      if (passiR != 0) {
        faiStep(passiR, pinR);
        Serial.print("muovo R di ");
        Serial.println(passiR);
      }
      if (passiF != 0) {
        faiStep(passiF, pinF);
        Serial.print("muovo F di ");
        Serial.println(passiF);
      }
      if (passiD != 0) {
        faiStep(passiD, pinD);
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

void faiStep(int passi, int mot[]) {
  if (passi < 0) {
    passi = 0 - passi;
    digitalWrite(mot[0], LOW);
  }
  else {
    digitalWrite(mot[0], HIGH);
  }
  if(mot[1]==10||mot[1]==12){
    analogWrite(mot[1], 255);
  }
  for (int i = 0; i < passi; i++) {
    digitalWrite(mot[1], HIGH);
    delayMicroseconds(ics);
    digitalWrite(mot[1], LOW);
    delayMicroseconds(ics);
  }
  if(mot[1]==10||mot[1]==12){
    analogWrite(mot[1], 0);
  }
}
