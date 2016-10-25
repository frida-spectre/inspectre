def main():
    import frida.repl
    import sys
    import json

    with open('./inspectre.json') as config_file:
        config = json.load(config_file)

    sys.argv = ['inspectre', '-f' ,config['target'], '-l', config['script']]
    if config['resumeOnStartup']:
        sys.argv.append('--no-pause')

    if config['quiet']:
        sys.argv.append('--quiet')

    frida.repl.main()

if __name__ == '__main__':
    main()