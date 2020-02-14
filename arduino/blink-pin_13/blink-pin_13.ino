//globals
int ledPin13 = 13; 
int count = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin13, OUTPUT);
   Serial.begin(9600);

}

void loop()
{
  for (int i =85; i <4000; i++)
  {
       digitalWrite(ledPin13, HIGH);
  delay(100);//on
  digitalWrite(ledPin13, LOW);
  delay(100);//off
  //task2
  digitalWrite(ledPin13, HIGH);
  delay(400);
  digitalWrite(ledPin13, LOW);
  delay(500);
  //task3
  digitalWrite(ledPin13, HIGH);
  delay(200);
  digitalWrite(ledPin13, LOW);
  delay(300);
  //task4
  digitalWrite(ledPin13, HIGH);
  delay(i);
  digitalWrite(ledPin13, LOW);
  delay(30);
    //task5
  digitalWrite(ledPin13, HIGH);
  delay(25);
  digitalWrite(ledPin13, LOW);
  delay(35);
    //task6
  digitalWrite(ledPin13, HIGH);
  delay(25);
  digitalWrite(ledPin13, LOW);
  delay(i);
    //task7
  digitalWrite(ledPin13, HIGH);
  delay(25);
  digitalWrite(ledPin13, LOW);
  delay(45);
     digitalWrite(ledPin13, LOW);
     delay(i);
     digitalWrite(ledPin13, HIGH);
     delay(i);
  }
  //end
  count++;
  Serial.println(" cm");
} 
