import glob
from pathlib import Path
from SpamBots.utils import load_plugins
import logging
from . import Legend, Legend2, Legend3, Legend4, Legend5, Legend6, Legend7, Legend8, Legend9, Legend10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "SpamBots/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")
print("Original Repo of: @OFFICIAL_SAMEER")
print("Modified By : @weTemp")
print("Also Join @LegendBot_Support")

if __name__ == "__main__":
    Legend.run_until_disconnected()
    
if __name__ == "__main__":
    Legend2.run_until_disconnected()

if __name__ == "__main__":
    Legend3.run_until_disconnected()
    
if __name__ == "__main__":
    Legend4.run_until_disconnected()

if __name__ == "__main__":
    Legend5.run_until_disconnected()
    
if __name__ == "__main__":
    Legend6.run_until_disconnected()

if __name__ == "__main__":
    Legend7.run_until_disconnected()
    
if __name__ == "__main__":
    Legend8.run_until_disconnected()

if __name__ == "__main__":
    Legend9.run_until_disconnected()
    
if __name__ == "__main__":
    Legend10.run_until_disconnected()

