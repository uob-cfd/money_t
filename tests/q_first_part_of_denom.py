test = {
  'name': 'Question first_part_of_denom',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'first_part_of_denom'
          >>> 'first_part_of_denom' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'first_part_of_denom'
          >>> # from its initial state (of ...)
          >>> first_part_of_denom is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.isclose(first_part_of_denom, 35318.038)
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
