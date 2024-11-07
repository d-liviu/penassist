# penassist

Penassist is a tool to help a pentester automate repetative, time consuming tasks are the exploration part of a client engagement. Freeing up more time, will allow the tester to use their creativity for other means rather that waiting for tools to return results.

[use cases](documentation/use-cases.md)

[goals](documentation/goals.md)


## Feature

### Quick Scan

Users can run a quick scan of a target system by using the flag `--quick-scan` 



### Full Scan

Users can run a full scan of a target system by using the flag `--full-scan` 



### Creating personalized configuration file
Users can create a personalized configuration file by using the flag `--create-config`

#### Example of configuration file

```
nmap:
  top_ports: 100
  aggressive_scan: false
ffuf:
  wordlist: /path/to/wordlist.txt
  threads: 10
```



## Installation

`pip install python-nmap`



## Usage

## Configuration

## Example

## Contributing

## License

## Contact
