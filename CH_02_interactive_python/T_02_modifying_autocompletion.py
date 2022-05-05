import __main__
import re
import atexit
import readline
import rlcompleter


class Completer(rlcompleter.Completer):

    ITEM_RE = re.compile(r'(?P<expression>.+?)\[(?P<key>[^\[]*)')

    def complete(self, text, state):
        # Init namespace. From `rlcompleter.Completer.complete`
        if self.use_main_ns:
            self.namespace = __main__.__dict__

        # If we find a [, try and return the keys
        if '[' in text:
            # At state 0 we need to prefetch the matches, after
            # that we use the cached results
            if state == 0:
                self.matches = list(self.item_matches(text))

            # Try and return the match if it exists
            try:
                return self.matches[state]
            except IndexError:
                pass
        else:
            # Fallback to the normal completion
            return super().complete(text, state)

    def item_matches(self, text):
        # Look for the pattern expression[key
        match = self.ITEM_RE.match(text)
        if match:
            search_key = match.group('key').lstrip()
            expression = match.group('expression')

            # Strip quotes from the key
            if search_key and search_key[0] in {"'", '"'}:
                search_key = search_key.strip(search_key[0])

            # Fetch the object from the namespace
            object_ = eval(expression, self.namespace)

            # Duck typing, check if we have a `keys()` attribute
            if hasattr(object_, 'keys'):
                # Fetch the keys by executing the `keys()` method
                # Can you guess where the bug is?
                keys = object_.keys()
                for i, key in enumerate(keys):
                    # Limit to 25 items for safety, could be
                    # infinite
                    if i >= 25:
                        break

                    # Only return matching results
                    if key.startswith(search_key):
                        yield f'{expression}[{key!r}]'


# By default readline doesn't call the autocompleter for [ because
# it's considered a delimiter. With a little bit of work we can
# fix this however :)
delims = readline.get_completer_delims()
# Remove [, ' and " from the delimiters
delims = delims.replace('[', '').replace('"', '').replace("'", '')
# Set the delimiters
readline.set_completer_delims(delims)

# Create and set the completer
completer = Completer()
readline.set_completer(completer.complete)
# Add a cleanup call on Python exit
atexit.register(lambda: readline.set_completer(None))
