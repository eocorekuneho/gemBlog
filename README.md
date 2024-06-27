# gemBlog

A small, really basic blogging system for hosting on Gemini protocol.

Can list files from a fixed folder, based on file modify date.

I made it just as a proof of concept for myself, but maybe someone find it useful. I think I'm gonna use it on my own capsule.

This code was made in a few hours, using nano in a terminal and the code itself isn't the cleanest and performance optimized...

Anyway.


## Configuration

Edit config.py. You can setup the following:

| Key                   | Description                                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------------------|
| GEMBLOG_ROOT          | Path to the folder that contains the .gmi files to list. Relative or absolute.                              |
| GEMBLOG_LANGUAGE      | Country code, this will be appended to the header on SUCCESS                                                |
| GEMBLOG_HEADER        | Title of your gemBlog. This will be at the top of the page, formatted as Header 1                           |
| GEMBLOG_HEADER2       | Subtitle of your gemBlog. This will be at the top of the page, under the title, formatted as Header 2       |
| GEMBLOG_INTRO         | Intro text of your gemBlog. This will be visible only on the index page.                                    |
| GEMBLOG_OUTRO         | Outro or footer of your gemBlog. This will be visible at the bottom of the page, formatted as regular text. |
| GEMBLOG_POSTS         | Label.                                                                                                      |
| GEMBLOG_RECENT        | Label.                                                                                                      |
| GEMBLOG_BACK          | Label.                                                                                                      |
| GEMBLOG_ENABLE_RECENT | If True, "Recent posts" block will be visible on the index page.                                            |
| GEMBLOG_RECENT_COUNT  | Number of posts to show in "Recent posts" block.                                                            |


## Usage
Right now, it is written with Jetforce (https://github.com/michael-lazar/jetforce) in mind. Just put it to your cgi-bin folder and make it executable.

If, for some reasone, there is no output visible in your gemini browser, you may need to wrap this inside a script.

```
#!/bin/bash
cd /path/to/gemblog
python3 gemblog.py

```

Make this executable and be this your endpoint.