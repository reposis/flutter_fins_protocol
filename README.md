<a href="https://reposis.com"><img src="https://reposis.com/logo.png" width="200" alt="Reposis Software" height="100"/></a>

# Flutter FINS Protocol

This package was developed to communicate with Omron PLCs that are in the same local network and use the FINS protocol.

## Installation

```bash
$ flutter pub add flutter_fins_protocol
```

## Usage

Currently all operations are done via Python using shell commands. Therefore Python needs to be installed. You can use the following command to check if it is installed and install it if it is not installed.

```dart
bool success = await Python.installScript();
if(success){
  //Commands to run if Python is installed
}
```

You can create an instance using the dynamicIp() and staticIp(String ip) static methods included in the FlutterFinsProtocol class, whichever suits you best.

```dart
FinsProtocolDynamic finsDynamic = FlutterFinsProtocol.dynamicIp();
FinsProtocolStatic finsStatic = FlutterFinsProtocol.staticIp("192.168.250.20");
```
You only need to define an IP once in the instances you create with staticIp. This is generally preferable when working with a single PLC.


If you need to communicate with more than one PLC continuously, you can choose to create an instance with dynamicIp. You need to specify the IP address for each operation (write, read etc.).
```dart
String result = await fins.write("192.168.250.20", MemoryAreas.DM, 100, [0, 4], 01);
print(result);
```


> **See the test folder for more examples.**

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU GPL v3.0](https://choosealicense.com/licenses/gpl-3.0/)