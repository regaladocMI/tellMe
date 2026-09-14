import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const TellMeApp());
}

class TellMeApp extends StatelessWidget {
  const TellMeApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'tellMe',
      theme: ThemeData(primarySwatch: Colors.indigo),
      home: const PantallaPrueba(),
    );
  }
}

class PantallaPrueba extends StatefulWidget {
  const PantallaPrueba({super.key});

  @override
  State<PantallaPrueba> createState() => _PantallaPruebaState();
}

class _PantallaPruebaState extends State<PantallaPrueba> {
  String _mensaje = 'Todavia no probaste la conexion.';

  Future<void> _probarConexion() async {
    try {
      final respuesta = await http.get(
        Uri.parse('http://10.0.2.2:8000/v1/ping'),
      );

      setState(() {
        _mensaje = respuesta.body;
      });
    } catch (error) {
      setState(() {
        _mensaje = 'Error de conexion: $error';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('tellMe')),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(_mensaje, textAlign: TextAlign.center),
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: _probarConexion,
                child: const Text('Probar conexion al backend'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}