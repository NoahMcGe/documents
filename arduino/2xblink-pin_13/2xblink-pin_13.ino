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
  digitalWrite(ledPin13, HIGH);
  delay(100);
  digitalWrite(ledPin13, LOW);
  delay(100);
  //task2
  digitalWrite(ledPin13, HIGH);
  delay(400);
  digitalWrite(ledPin13, LOW);
  delay(500);
  //end
  count++;
  Serial.println(" cm");
} 
