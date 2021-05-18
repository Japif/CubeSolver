void setup() {
  Serial.begin(2400);
  pinMode(13, OUTPUT);
  pinMode(A0, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
}
String specMove = "";
String finalString = "";
char moveArray [200];
int arrayCounter = 0;
int i;
int k;
int typeMove(char);
int up = 12;
int down = 2;
int right = 4;
int back = 6;
int left = 8;
int front = 10;
int Ybuffer = 0;
int Xbuffer = 0;
bool exitCond = false;
void loop() {
  delay(1000);
  while (!Serial.available()){
      Serial.println("waiting for input");
      delay(1000);
    }
  /*while (Serial.available()) {
      specMove = (char)Serial.read();
      finalString.concat(specMove);
      arrayCounter++;
      delay(10);
    }
   */
  finalString = "UUiXXXUUio";
  Serial.println(finalString);
  finalString.toCharArray(moveArray, 200);
  Serial.println(arrayCounter);
  digitalWrite(A0, HIGH);
  delay(500);
  for (i=0; i<198; i++){
      Serial.println(moveArray[i]);
      switch (moveArray[i]) {
        case 'U':
            digitalWrite(up+1, HIGH);
            Serial.println("MOVING U");
            if(typeMove(moveArray[i+1]) == 1){
              digitalWrite(up+1, LOW);
            }
            doMove(up);
            digitalWrite(up+1, LOW);
          break;

        case 'L':
          digitalWrite((left+1), HIGH);
          Serial.println("MOVING L");
          if(typeMove(moveArray[i+1]) == 1){
              digitalWrite((left+1), LOW);
            }
            doMove(left);
            digitalWrite((left+1), LOW);
          break;

        case 'B':
            digitalWrite((back+1), HIGH);
            Serial.println("MOVING B");
            if(typeMove(moveArray[i+1]) == 1){
              digitalWrite((back+1), LOW);
            }
            doMove(back);
            digitalWrite((back+1), LOW);
          break;

        case 'R':
            digitalWrite((right+1), HIGH);
            Serial.println("MOVING R");
            if(typeMove(moveArray[i+1]) == 1){
              digitalWrite((right+1), LOW);
            }
            doMove(right);
            digitalWrite((right+1), LOW);
          break;

        case 'F':
            digitalWrite((front+1), HIGH);
            Serial.println("MOVING F");
            if(typeMove(moveArray[i+1]) == 1){
              digitalWrite((front+1), LOW);
            }
            doMove(front);
            digitalWrite((front+1), LOW);
          break;

        case 'D':
            digitalWrite((down+1), HIGH);
            Serial.println("MOVING D");
            if(typeMove(moveArray[i+1]) == 1){
              digitalWrite((down+1), LOW);
            }
            doMove(down);
            digitalWrite((down+1), LOW);
          break;

        case 'X':
            Xbuffer = up;
            up = front;
            front = down;
            down = back;
            back = Xbuffer;
          break;
          
        case 'Y':
            Ybuffer = right;
            right = back;
            back = left;
            left = front;
            front = Ybuffer;
          break;

        case 'i':
          break;
        case 'o':
          exitCond = true;
        default:
          break;
      }
     if(exitCond == true){
      break;
     }
    }
    digitalWrite(A0, LOW);
    while(1){
      delay(1000);
    }
}

void doMove(int pinNum){
  for(k=0;k<50;k++){
      digitalWrite(pinNum, HIGH);
      delayMicroseconds(800);
      digitalWrite(pinNum, LOW);
      delayMicroseconds(800);
  }
  delay(100);
}
int typeMove(char next){
    if(next == 'i'){
      return 1;
    }
    else{
      return 0;
    }
}
