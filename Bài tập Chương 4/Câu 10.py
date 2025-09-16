import time
import os

shapes = [
    """
      *
      * * 
      * * * 
* * * * * * * 
* * *
* *
*
""",
    """
      *
      * * 
      *   * 
* * * * * * * 
*  *
* *
*
""",
    """
      * * * *
      * * *
      * *
      *
    * *
  * * *
* * * *
""",
    """
      * * * *
      *   *
      * *
      *
    * *
  *   *
* * * *
"""
]

for s in shapes:
    os.system("cls" if os.name == "nt" else "clear")
    print(s)
    time.sleep(5)
