from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Bug: even-attempt string coercion causes wrong hints for negative numbers ---

def test_negative_guess_below_secret_is_too_low():
    # "-5" < "50" lexicographically is True, but this should still be Too Low numerically
    result = check_guess(-5, 50)
    assert result == "Too Low"

def test_negative_guess_above_negative_secret_is_too_high():
    # -1 is numerically greater than -10, must not be misled by string comparison
    result = check_guess(-1, -10)
    assert result == "Too High"


# --- Bug: secret passed as str on even attempts causes wrong hints ---

def test_winning_guess_string_secret():
    # On even attempts the app passes secret as str — equality must still hold
    result = check_guess(50, "50")
    assert result == "Win"

def test_guess_too_high_string_secret():
    # 80 > int("50"), so must return Too High even when secret is a str
    result = check_guess(80, "50")
    assert result == "Too High"

def test_guess_too_low_string_secret():
    # 30 < int("50"), so must return Too Low even when secret is a str
    result = check_guess(30, "50")
    assert result == "Too Low"


# --- Bug: even-attempt string coercion flips hint direction ---
# On even attempts, secret was cast to str, causing lexicographic comparison.
# e.g. secret=29, guess=10 → "10" > "29" is True lexicographically → wrong "Too High" hint

def test_even_attempt_coercion_low_guess():
    # guess=10, secret="29" (as str) — "10" > "29" lexicographically, so buggy code returns Too High
    # correct answer is Too Low
    result = check_guess(10, "29")
    assert result == "Too Low"

def test_even_attempt_coercion_high_guess():
    # guess=50, secret="29" (as str) — "50" > "29" lexicographically, this one accidentally correct
    # but must be verified it returns Too High for the right reason (numeric, not lexicographic)
    result = check_guess(50, "29")
    assert result == "Too High"

def test_even_attempt_coercion_win():
    # guess=29, secret="29" (as str) — must still be a Win despite string secret
    result = check_guess(29, "29")
    assert result == "Win"


# --- Bug: guessing 100 returns "Too High" hint erroneously ---

def test_guess_100_wins_when_secret_is_100():S
    result = check_guess(100, 100)
    assert result == "Win"

def test_guess_100_is_too_high_when_secret_is_below():
    # 100 > 50 numerically, hint must be Too High (not flipped by string coercion)
    result = check_guess(100, 50)
    assert result == "Too High"