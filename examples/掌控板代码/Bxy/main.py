# 功能：发布光线数据    from mpython import lightfrom Iot import Iotfrom umqtt.simple import MQTTClientfrom machine import Timerimport machineimport timeimport jsonimport networkWIFI_SSID = 'yourSSID'#替换成你的WIFI热点名称WIFI_PASSWORD = 'yourPASSWD'#替换成你的WIFI热点密码EASYIOT_SERVER = "192.168.1。135"EASYIOT_PORT = 1883ClientID = "your ClientID"#替换成你的EasyIot的ClientIDUserName = "your UserName"#替换成你的EasyIot设备UserNamePassWord = "your PassWord"#替换成你的EasyIot设备PassWordpubTopic = 'your Topic'myIot = Iot(EASYIOT_SERVER, UserName, ClientID, PassWord)client = MQTTClient(myIot.client_id, myIot.mqttserver, port = EASYIOT_PORT, user = myIot.username, password = myIot.password)tim1 = Timer(1)def connectWIFI():  station = network.WLAN(network.STA_IF)  station.active(True)  station.connect(WIFI_SSID,WIFI_PASSWORD)  while station.isconnected() == False:    pass  print('Connection successful')  print(station.ifconfig())  def restart():  time.sleep(10)  machine.reset()  def check(_):  try:    msg = {}    client.check_msg()    msg["light"] = light.read()    print(json.dumps(msg))    client.publish(pubTopic,json.dumps(msg))    lastTime = time.time()  except OSError as e:    tim1.deinit()    restart()  connectWIFI()client.connect()tim1.init(period=5000, mode=Timer.PERIODIC,callback=check)while True:  pass