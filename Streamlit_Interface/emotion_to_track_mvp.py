import random

# Dictionary mapping emotions to lists of Spotify track IDs
emotion_tracks = {
    'happy': [
        '0VjIjW4GlUZAMYd2vXMi3b', '3w3y8KPTfNeOKPiqUTakBh', '4uUG5RXrOk84mYEfFvj3cK', '4h9wh7iOZ0GGn8QVp4RAOB', '1zi7xx7UVEFkmKfv06H8x0',
        '1mea3bSkSGXuIRvnydlB5b', '6UelLqGlWMcVH1E5c4H7lY', '7qiZfU4dY1lWllzX7mPBI3', '7JJmb5XwzOO8jgpou264Ml', '0ct6r3EGTcMLPtrXHDvVjc',
        '3ZFTkvIE7kyPt6Nu3PEa7V', '7BqBn9nzAq8spo5e7cZ0dJ', '2tpWsVSb9UEmDRxAl1zhX1', '0FDzzruyVECATHXKHFs9eJ', '4cluDES4hQEUhmXj6TXkSo',
        '4QNpBfC0zvjKqPJcyqBy9W', '4HlFJV71xXKIGcU3kRyttv', '2ENexcMEMsYk0rVJigVD3i', '0azC730Exh71aQlOt9Zj3y', '0HPD5WQqrq7wPWR7P7Dw1i',
        '50nfwKoDiSYg8zOCREWAm5', '6UjZ1oYpXUOaEfCXsTnXiP', '6Kv8FqUL5oRtXnMQfMbK6e', '6l6HeuYUpl1VJjwcXUpCjz', '5kD9T7GForh8LnRz5ClbL8',
        '3Af6QIoFMEqawYpaCP8tJ7', '4eXB5pavwlO3ejMypFgVsv', '6BZ3hhOkAIDGMGQNueZ5GG', '6vocnqTDG1lKO3orAp3LRR', '3bjBeyazbIgFgXYPoQK4UH',
        '5zEJbVbOY5rRPTFD30PjfO', '0PgLNhpBCMx4d04FEP7q23', '3vZ3kW9o4v9bmb2b0o8PCg', '2jvdgmCVS2ztUWE5bIfxRb', '1nMMR4bAPJYvDcBciwOv2F',
        '0ZpiNU0E1ILADs2ODMSKpA', '6F608N6iuoO3dReb1nCMmO', '5HpxjB5QM6Fx0N56mYA5l4', '3Wh4aB60udsy7qZPQgqTaT', '0CokSRCu5hZgP6XPoIz0iO',
        '5jzma6gCzYtKB1DbEwFZKH', '4D6uG5THdO9tZpOPgKN7vu', '5vGlqQANWDKJFl0MBG3sg2', '19D3flTGGtzkHCtGVfG6qH', '3qHMlZfTQzGQVbzHf3GhwO',
        '3MEa4GuewpYRUBAjk3c2ov', '4H2g0YX7AebFZJ3ylT3tCA', '1s26cVgDS5xoPWNHWBAHYu', '6Y2r6Qqw0zrDwXrIIwZ6T8', '3Er2q0jItcp8HIVYHEdrEr',
        '1HHe0fGgrbBvGtPkIAv5K8', '44cJEtVQT2jNQV4jBYL8Tf', '7DnPf6MlOZbZgAVNEU7BZ3', '0cGHiaT4qUKMyfx5UOHw1T', '4SywM4HF3QltBCv7xRmqzJ',
        '3PgzrQIulOiqsVk3Ckqzde', '5W83ErFkO3aKAIS1WMi6u0', '5HCyWlXZPP0y6Gqq8TgA20', '5KawlOMHjWeUjQtnuRs22c', '2Rk4JlNc2TPmZe2af99d45',
        '5a6PD9k4poeA7cA54C18mE', '2RttW7RAu5nOAfq6YFvApB', '7lQWRAjyhTpCWFC0jmclT4', '1Yy5eDys3LWl8IAhRplp1R', '37KFiVtY5jNJEdyftDQrPb',
        '0V6gREQL5ynP9eYZOvQh7M', '2QjOHCTQ1Jl3zawyYOpxh6', '3KPVQltGw9fId3cRLDCGtG', '2BcMwX1MPV6ZHP4tUT9uq6', '4lUmnwRybYH7mMzf16xB0y',
        '3K9T8JWYrBShp4iIQUmO4M', '78WgTPUsFNLtCgKjIvARnA', '0PJIbOdMs3bd5AT8liULMQ', '0ppAGdFxr4NHGXlm4FzjOV', '7gq1OB2zB80u77Ly9W8r1r'
    ],
    'neutral': [
        '1SadNNfKugUYlaXTZO9g7c', '2LeF018m9vGgIAirUuOgCr', '0WVVyFVPOK3ATwptxglXHZ', '043xe58AMUGPJgCnRJynj9', '1mANYloG5MWO9OYzt7pCu9',
        '2uio4eJ81UkXTHGbK99ebr', '3HtEAL9JC5o1aaS0drr4fk', '7lQop4kJwVavS9JXVVZdiv', '6aJmkGMF1xcrcviZbn1n0R', '08PythMQ97nIacc0AdIdnP',
        '2FWz4GoP0aTNym0kjLZ5gI', '7oXwwzULPtCZHT7eCkXxIC', '5iPB9VskHHAsEcpOf4dpxw', '5jnQVTGkb8rDOMbX6kOqFH', '0BBtNOB7ofrOJ9PLM74EQn',
        '3S0NnkTIk3LbDoL8dUY1Tc', '4jGz7wyQknFLmTgvvNJyrE', '3vdpuNfchEDUQNOdtPB0FS', '0GdZ6vlb3nC8t5B5MP6TqP', '14BAmiynFdqR5mTp6yd6d9',
        '1KuLyZWT9FbLsFGsi6LpXU', '6eQmbEMHQYPkRj44AWf04Q', '6VzShi66jALkxxTgCCCspZ', '0aYsYUlByBk66OJNHK9QxC', '0HoWhKBcNCjomwXVCg5Mcz',
        '5iGa3KHzFg7CtCfpqqY0Cp', '6mCHWvDL7kXZdVhc8ovk0y', '2szpAFtTaGmAdXaXpfzHof', '0ghzP8Reit8lJhU85KLqzq', '2r20uyktL1iCiwXIBN19ok',
        '1OmGQ1LqE8o3YQTRPKOMiC', '1M3aJGASviOoIwX6Ndh6sI', '3AulsDX9Fz7t1Iy9GB51pB', '5BpqczsIDRdI8Sjg3muSeB', '5cnwPn0MKDPnu2rUamIRgb',
        '6QCZUHBxTk7Fa05l0RFhMn', '3UwfJUXOIYLhGElSoteZvE', '4YzZwV3CsUsT2orcj9yTUg', '5ORMaylKqIYBtAFedOVIXD', '6t0ihkmPbunxNnAzs45AZM',
        '54Q1fME5hhgFWipi1SkTtU', '1dnSIg4ulPAEIWDmuWA5Cf', '3XxZiDTQflprBVjBFxG6qH', '66fThwu8rpOl0CDMLZzeTg', '4oikNLzA8VDnsEXrsiHQA9',
        '3ctgxH0ZpE50qscnZYBY1H', '1TDDBPg0JCXBdq6kpnbOG0', '63q1ZAwIpU7IahDGxU7QZV', '0jaGw9MKg6t9z9wfzWAK0a', '3UWWuXut5dDfLA6gDL5H8S',
        '5TC2wrYzGhhr1wO7BSsGOA', '5pbMjvDEHdFVRkxjNeaUFu', '5HiTU06li1OKrzNue6Vt4K', '0gDrjkBGC61kkPHJhKyctN', '0e7Zh5sczPvNV40Y9f5ujE',
        '1AqN43ZIZzz74aAtnsovZ1', '1vwVgDd0EHURAjoTb2glnM', '0WZmg03i0vltH03r3pDuex', '1divZI9KtgP416oHCwBJE1', '7xJqP2LZrVpJhUR6ZukE9q',
        '2SIG8r7jJLXc9Q3fAOUrwx', '18te6JAwwL6xrKnVgYgXvA', '5AColl6xt8Gnm8fNG05hO', '0AcP7ZjBbsoB2VVdPJfGOA', '5RTEnxaWcMizgabaUxWQ7K',
        '0LgXKAaGOJBUgB1eiVQVzo', '0bnUDXvwi2s8924tLTDg3K', '2qLyo5FeWquE7HBUbcVnEy', '1ovZe7upcqycTuPFfOg6kB', '7MOCaEUbfGyq1K96umNVwJ',
        '2DjZwbUsZeLL7qzyej7K0V', '1Jt24MPLz6fGXSCTlXTjzF', '7uo2L5FAja3pWIBa3HJVeC', '5WMA8AmXGff8wo450I3Ecn', '1z7PADWKXVsbEitOVLlC69',
        '3PhzwF9SOkkMIoUSIxFtwo', '1mBtrVS6hLeqcVecvpAqBJ', '74eJR4gwG1ZmG4BFkbrOlA', '3iJVCCW5equhyyZcxrMABz', '3hUxzQpSfdDqwM3ZTFQY0K',
        '24dotUzOINUEH3iTUlhDXX', '0YywjDvFudcaHG74NuWISy', '0gplL1WMoJ6iYaPgMCL0gX', '5hnGrTBaEsdukpDF6aZg8a', '4nyF5lmSziBAt7ESAUjpbx'
    ],
    'sad': [
        '1ei3hzQmrgealgRKFxIcWn', '6wf7Yu7cxBSPrRlWeSeK0Q', '1Fid2jjqsHViMX6xNH70hE', '1odExI7RdWc4BT515LTAwj', '1XTY6rA7XQosc0ynkkE9kN',
        '4Y9ZFT6aD1PfZJHLZXi9EQ', '3XloH0C8QYXgbYPmXlxf2x', '0YywjDvFudcaHG74NuWISy', '0gplL1WMoJ6iYaPgMCL0gX', '5hnGrTBaEsdukpDF6aZg8a',
        '4nyF5lmSziBAt7ESAUjpbx', '4IhTXiZLKATmwhMZIb1GQN', '7nku4ywsysUidKcPiS4hIQ', '7l97ElWmIdVHWUaOeeU5ZC', '2Kqw2ECnErSCU9bxPSVgGx',
        '6ErCfbbI9BG4bK2djjKUvH', '4KULAymBBJcPRpk1yO4dOG', '3Nl5OkkmS5DaBZvuYofpAt', '2TwdK6m9dTg2L8oKhZC7ZD', '3JvKfv6T31zO0ini8iNItO',
        '7dDrR6vMK1JAwZZ5MIWgme', '4Skkx52Dh8yo4G1ijAEGs3', '7qqOrc0Uvpvl5NvoAPRGLE', '34dVuWyRUgApvlec3hlqic', '22UYp7aAy1XmIYZ1GsnJuB',
        '4RL77hMWUq35NYnPLXBpih', '4xqrdfXkTW4T0RauPLv3WA', '3gdPwk2wyOXNRnTA1KXnEr', '0V9QY6NnXtAMwjltgMP0pl', '3vkCueOmm7xQDoJ17W1Pm3',
        '6eI8B3QW20P68MCYMb4Etd', '68CijBYyD89CISS4vDLAaq', '5uu2OCGGrTRS1sIvlMgKwe', '5aXfGM7WVcqyAvqnL7k0y3', '7wB9sL81rFRGhRt6msZ9CV',
        '1kuGVB7EU95pJObxwvfwKS', '7slfeXbuzr9RYXX6XS6Npi', '7CiDwKE62N6ey3LyG6s7xc', '7D0RhFcb3CrfPuTJ0obrod', '0otRX6Z89qKkHkQ9OqJpKt',
        '6wpOHVSrinXhKqF4EBbpuS', '3rAZYyztPLBaQ7TTXdxk7m', '04zpnoSROKFTCfgkoPcZ5A', '3UrmjZcjcYP3zFUdfWOy46', '3t5o6aDBXWyNZiyFQylraq',
        '3yMC1KsTwh0ceXdIe4QQAQ', '135Lf4Q0CzlMNfOxbEUsLH', '3jc0jdopFsv3dYz5uo8OCr', '3ZBeHiRJUj1vdiU8zzGPgb', '6gPPoRYJwCsoB2VVdPJfmo',
        '5gukv8x9eP58gFy2OcZEBQ', '0gOz9JUXsaKVzLTSmFDtdo', '7MOCaEUbfGyq1K96umNVwJ', '2DjZwbUsZeLL7qzyej7K0V', '1Jt24MPLz6fGXSCTlXTjzF',
        '7uo2L5FAja3pWIBa3HJVeC', '5WMA8AmXGff8wo450I3Ecn', '1z7PADWKXVsbEitOVLlC69', '3PhzwF9SOkkMIoUSIxFtwo', '1mBtrVS6hLeqcVecvpAqBJ',
        '74eJR4gwG1ZmG4BFkbrOlA', '3iJVCCW5equhyyZcxrMABz', '3hUxzQpSfdDqwM3ZTFQY0K', '24dotUzOINUEH3iTUlhDXX', '0YywjDvFudcaHG74NuWISy',
        '0gplL1WMoJ6iYaPgMCL0gX', '5hnGrTBaEsdukpDF6aZg8a', '4nyF5lmSziBAt7ESAUjpbx', '4IhTXiZLKATmwhMZIb1GQN', '7nku4ywsysUidKcPiS4hIQ',
        '7l97ElWmIdVHWUaOeeU5ZC', '2Kqw2ECnErSCU9bxPSVgGx', '6ErCfbbI9BG4bK2djjKUvH', '4KULAymBBJcPRpk1yO4dOG', '3Nl5OkkmS5DaBZvuYofpAt'
    ]
}

def get_random_track_embed_code(emotion):
    """
    Get the embed code for a random track based on the input emotion.

    Parameters:
    - emotion (str): The emotion for which to get a random track. Must be 'sad', 'happy', or 'neutral'.

    Returns:
    - str: The embed code for the random track.

    Raises:
    - ValueError: If the input emotion is not valid.
    """
    if emotion not in emotion_tracks:
        raise ValueError("Invalid emotion. Please choose 'sad', 'happy', or 'neutral'.")

    track_id = random.choice(emotion_tracks[emotion])
    embed_code = f'<iframe src="https://open.spotify.com/embed/track/{track_id}" width="700" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'

    return embed_code,track_id
