test = {
  'name': 'Question like_t',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'like_t'
          >>> 'like_t' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'like_t'
          >>> # from its initial state (of ...)
          >>> like_t is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # See simulate_like_t.py for limits.
          'code': r"""
          >>> 1.74 < like_t < 1.85
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
