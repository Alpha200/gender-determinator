# Gender Determinator

Determines the gender of german nouns and provides some convenient methods.

## Usage

```python
from genderdeterminator import GenderDeterminator, Case

gd = GenderDeterminator()

print(gd.get_gender("Garten"))           # prints "m"
print(gd.get("Garten", Case.NOMINATIVE)) # prints "der Garten" 
```

Gender determinator uses the eng-deu dictionary by [FreeDict](https://freedict.org/) to determine the genders.