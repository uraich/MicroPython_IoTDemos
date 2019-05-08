/**
 * @file cayenneBuzzer.c
 *
 * A simple QT application that sends a song number to Cayenne
 * This song number is picked up by an IoT node connected to Cayenne as well and subscribed
 * to the topic corresponding to the song number.
 * The node then selects the song and plays it on its passive buzzer
 * This program is part of the workshop on IoT at the
 * African Internet Summit 2019, Kapala, Uganda
 * Copyright U. Raich
 * The program is released under GPL
 */
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QStringListModel>
#include <QDebug>
#include "CayenneMQTTClient.h"
#include <unistd.h>

// Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
char* username = (char *)"7c70a330-69af-11e8-a76a-fdebb8d0010d";
char* password = (char *)"32d184add41570759dd1735fa464cef7e62876a4";
char* clientID = (char *)"4dde8070-593f-11e9-bb1a-97096e6377d3";

Network network;
CayenneMQTTClient mqttClient;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    // Initialize the network.
    NetworkInit(&network);

    // Initialize the Cayenne client.
    CayenneMQTTClientInit(&mqttClient, &network, username, password, clientID, NULL);

    // Connect to Cayenne.
    if (connectClient() != CAYENNE_SUCCESS) {
        printf("Connection failed, exiting\n");
        exit(-1);
    }

    ui->setupUi(this);

    // Create model
    QStringListModel *model = new QStringListModel(this);
    QStringList List;

    List << "Super Mario - Main Theme";
    List << "Super Mario - Title Music";
    List << "SMBtheme";
    List << "SMBwater";
    List << "SMBunderground";
    List << "The Simpsons";
    List << "Indiana";
    List << "TakeOnMe";
    List << "Entertainer",
    List << "Muppets";
    List << "Xfiles";
    List << "Looney";
    List << "20thCenFox";
    List << "Bond";
    List << "MASH";
    List << "StarWars";
    List << "GoodBad";
    List << "TopGun";
    List << "A-Team";
    List << "Flinstones";
    List << "Jeopardy";
    List << "Smurfs";
    List << "MahnaMahna";
    List << "LeisureSuit";
    List << "MissionImp";

    // Populate our model
    model->setStringList(List);
    // Glue model and view together
    ui->listView ->setModel(model);
    ui->listView->setSelectionMode(QAbstractItemView::SingleSelection);
    connect(ui->playButton, SIGNAL(clicked()),this,SLOT(slotPlay()));
}


MainWindow::~MainWindow()
{
    delete ui;
}
// Connect to the Cayenne server.
int MainWindow::connectClient(void)
{
    // Connect to the server.
    int error = 0;
    printf("Connecting to %s:%d\n", CAYENNE_DOMAIN, CAYENNE_PORT);
    if ((error = NetworkConnect(&network, (char *)CAYENNE_DOMAIN, CAYENNE_PORT)) != 0) {
        return error;
    }

    if ((error = CayenneMQTTConnect(&mqttClient)) != MQTT_SUCCESS) {
        NetworkDisconnect(&network);
        return error;
    }
    printf("Connected\n");

    return CAYENNE_SUCCESS;
}

void MainWindow::slotPlay(void)
{
    qDebug() << "Playing the song";

    int selected = ui->listView->currentIndex().row();
//    QString selString = "Song No " + QVariant(selected).toString();
    qDebug() << "Song number: " << selected;
    if (selected < 0)
        return;
    CayenneMQTTPublishDataInt(&mqttClient, NULL, COMMAND_TOPIC, 1,
                              TYPE_ANALOG_ACTUATOR, UNIT_UNDEFINED , selected+1);
}
