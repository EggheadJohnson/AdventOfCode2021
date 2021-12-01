// import '/home/paul/.pub-cache/hosted/pub.dartlang.org/args-2.3.0/lib/args.dart'; // This doesn't work on Mac
import '/Users/pejohnson/.pub-cache/hosted/pub.dartlang.org/args-2.3.0/lib/args.dart'; // This doesn't work on Linux

String getFileName(List<String> arguments) {
  var parser = ArgParser();
  parser.addFlag('puzzle', abbr: 'p', defaultsTo: false);

  var results = parser.parse(arguments);

  if (results['puzzle']) {
    return 'puzzle.txt';
  }
  return 'sample.txt';
}
