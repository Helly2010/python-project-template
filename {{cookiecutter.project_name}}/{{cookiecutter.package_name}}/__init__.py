__version__ = "
{%- if cookiecutter.version_pattern == 'YYYY0M.BUILD[-TAG]' -%}
{% now 'utc', '%Y%m' %}.1001
{%- elif cookiecutter.version_pattern == 'MAJOR.MINOR.PATCH[PYTAGNUM]' -%}
0.1.0
{%- endif -%}
"
