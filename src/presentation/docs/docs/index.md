<html>
    <head>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/modest.css') }}">
    </head>
    <div class='content'>
{% filter markdown %}

# VeaChron Documentation #
This is the documentation page for the timing application VeaChron. 

## Installation ##
VeaChron can be installed by ...

## Use ##
To use VeaChron ...

{% endfilter %}
    </div>
</html>