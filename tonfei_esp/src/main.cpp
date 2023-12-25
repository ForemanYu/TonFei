#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>


// WIFI LED GPIO 5 D4
#define LED 2  //定义宏或常量

// WiFi
const char *ssid = "TP-LINK_BD30";
const char *password = "88888888";

// MQTT Broker
const char *mqtt_broker = "broker.emqx.io";
const char *topic = "esp8266/tonfei";
const char *mqtt_username = "emqx";
const char *mqtt_password = "public";
const int mqtt_port = 1883;

bool ledState = false;

WiFiClient espClient;
PubSubClient client(espClient);

void callback(char *topic, byte *payload, unsigned int length) {
    Serial.print("Message arrived in topic: ");
    Serial.println(topic);
    Serial.print("Message: ");
    String message;
    for (unsigned int i = 0; i < length; i++) {
        message += (char) payload[i];  // Convert *byte to string
    }
    Serial.print(message);
    if (message == "on" && !ledState) {
        digitalWrite(LED, HIGH);  // Turn on the LED
        ledState = true;
    }
    if (message == "off" && ledState) {
        digitalWrite(LED, LOW); // Turn off the LED
        ledState = false;
    }
    Serial.println();
    Serial.println("------");
}


void setup() {
    pinMode(LED, OUTPUT); // 设置成输出模式

    // 将软件串行波特设置为 115200;
    Serial.begin(115200);
    // 连接到 WiFi 网络
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to the WiFi network");

    //连接到 MQTT 代理
    client.setServer(mqtt_broker, mqtt_port);
    client.setCallback(callback);
    while (!client.connected()) {
        String client_id = "esp8266_client_";
        client_id += String(WiFi.macAddress());
        Serial.printf("The client %s connects to the public MQTT broker\n", client_id.c_str());
        if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) {
            Serial.println("Public EMQX MQTT broker connected");
        } else {
            Serial.print("Failed with state ");
            Serial.print(client.state());
            delay(2000);
        }
    }

    // 发布和订阅
    client.publish(topic, "hello emqx ");
    client.subscribe(topic);
}

void loop() {
    client.loop();
    delay(100); //在每次循环迭代中延迟一小段时间

//    digitalWrite(LED, HIGH);
//    delay(1000);
//    digitalWrite(LED, LOW);
//    delay(1000);
}
