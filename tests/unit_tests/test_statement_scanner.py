from . import StatementScanner, Token, TokenType


def test_statement_scanner_can_be_created():
    scanner = StatementScanner("")
    assert scanner is not None


def test_statement_scanner_expected_simple_scan_results():
    src = "<+=()"
    scanner = StatementScanner(src)
    tkns = scanner.scan_tokens()
    assert len(scanner.tokens) == len(src) + 1
    # for t in tkns:
    #     print(t.to_string())
    assert tkns[0].type == TokenType.LT
    assert tkns[1].type == TokenType.PLUS
    assert tkns[2].type == TokenType.EQ
    assert tkns[3].type == TokenType.LEFT_PAREN
    assert tkns[4].type == TokenType.RIGHT_PAREN
    assert tkns[5].type == TokenType.EOF


def test_scanner_match_method_returns_expected_results():
    src = "< <= => >="
    tkns = _tkns(src)
    # for t in tkns:
    #     print(t.to_string())
    assert tkns[0].type == TokenType.LT
    assert tkns[1].type == TokenType.LT_OR_EQ
    assert tkns[2].type == TokenType.EQ
    assert tkns[3].type == TokenType.GT
    assert tkns[4].type == TokenType.GT_OR_EQ
    assert tkns[5].type == TokenType.EOF


def test_scanner_caseLT():
    src = "< <= "
    tkns = _tkns(src)
    assert tkns[0].type == TokenType.LT
    assert tkns[1].type == TokenType.LT_OR_EQ
    assert tkns[2].type == TokenType.EOF


def test_scanner_caseGT():
    src = "> >= "
    tkns = _tkns(src)
    assert tkns[0].type == TokenType.GT
    assert tkns[1].type == TokenType.GT_OR_EQ
    assert tkns[2].type == TokenType.EOF


def test_scanner_caseEQ():
    src = "= == "
    tkns = _tkns(src)
    assert tkns[0].type == TokenType.EQ
    assert tkns[1].type == TokenType.EQEQ
    assert tkns[2].type == TokenType.EOF


def test_scanner_caseBANG():
    src = "! != "
    tkns = _tkns(src)
    assert tkns[0].type == TokenType.BANG
    assert tkns[1].type == TokenType.BANG_EQ
    assert tkns[2].type == TokenType.EOF


def test_scanner_caseNUMBER():
    src = "12 2.5"
    tkns = _tkns(src)
    # for t in tkns:
    #     print(t.to_string())
    assert tkns[0].type == TokenType.NUMBER
    assert tkns[1].type == TokenType.NUMBER
    assert tkns[2].type == TokenType.EOF
    assert tkns[0].lexeme == 12.0
    assert tkns[1].lexeme == 2.5


def test_scanner_swtich_is_alpha():
    scanner = _scn("")
    sw = scanner.switch
    assert sw.is_alpha("a") == True
    assert sw.is_alpha("Z") == True
    assert sw.is_alpha("g") == True
    assert sw.is_alpha("3") == False
    assert sw.is_alpha("") == False
    assert sw.is_alpha(" ") == False
    assert sw.is_alpha("\\") == False
    assert sw.is_alpha("_") == True


def test_scanner_switch_is_digit():
    scanner = _scn("")
    sw = scanner.switch
    assert sw.is_digit("9") == True
    assert sw.is_digit("1") == True
    assert sw.is_digit("2") == True
    assert sw.is_digit("3") == True
    assert sw.is_digit("") == False
    assert sw.is_digit("p") == False
    assert sw.is_digit("$") == False


def test_scanner_switch_peek_and_next():
    src = "012"
    scanner = _scn(src)
    sw = scanner.switch
    assert sw.peek() == "0"
    assert sw.peek_next() == "1"
    # increment and peek again
    scanner.current = 1
    assert sw.peek() == "1"
    assert sw.peek_next() == "2"
    src_2 = "=+1"
    scanner_2 = _scn(src_2)
    sw_2 = scanner_2.switch
    assert sw_2.peek() == "="
    assert sw_2.peek_next() == "+"
    scanner_2.current = 1
    assert sw_2.peek() == "+"
    assert sw_2.peek_next() == "1"


def test_scanner_switch_caseIDENTIFIER():
    src = "=!test test123"
    tkns = _tkns(src)
    assert tkns[0].type == TokenType.EQ
    assert tkns[1].type == TokenType.BANG
    assert tkns[2].type == TokenType.IDENTIFIER
    assert tkns[2].lexeme == "test"
    assert tkns[3].type == TokenType.IDENTIFIER
    assert tkns[3].lexeme == "test123"
    assert tkns[4].type == TokenType.EOF


def test_scanner_switch_caseIDENTIFIER_with_keywords():
    src = "=!test Close test123"
    tkns = _tkns(src)
    assert tkns[0].type == TokenType.EQ
    assert tkns[1].type == TokenType.BANG
    assert tkns[2].type == TokenType.IDENTIFIER
    assert tkns[2].lexeme == "test"
    assert tkns[3].type == TokenType.CLOSE
    assert tkns[3].lexeme == "Close"
    assert tkns[4].type == TokenType.IDENTIFIER
    assert tkns[4].lexeme == "test123"
    assert tkns[5].type == TokenType.EOF


def test_scanner_switch_caseIDENTIFIER_with_keywords_indicator():
    src = "Close < SMA(200)"
    tkns = _tkns(src)
    assert len(tkns) == 4
    assert tkns[0].type == TokenType.CLOSE
    assert tkns[1].type == TokenType.LT
    assert tkns[2].type == TokenType.SMA
    assert tkns[3].type == TokenType.EOF
    _debug_tkns(tkns, False)


def test_scanner_switch_caseIDENTIFIER_with_keywords_indicator_days_ago():
    src = "Close < three days ago SMA(200)"
    tkns = _tkns(src)
    assert len(tkns) == 7
    assert tkns[0].type == TokenType.CLOSE
    assert tkns[1].type == TokenType.LT
    assert tkns[2].type == TokenType.THREE
    assert tkns[3].type == TokenType.DOMAIN_INDEX
    assert tkns[4].type == TokenType.DAILY
    assert tkns[5].type == TokenType.SMA
    assert tkns[6].type == TokenType.EOF
    _debug_tkns(tkns, False)


def test_scanner_switch_caseIDENTIFIER_with_keywords_time_frame_numbers():
    src = "two days ago Close"
    tkns = _tkns(src)
    # _debug_tkns(tkns)
    assert len(tkns) == 5
    assert tkns[0].type == TokenType.TWO
    assert tkns[1].type == TokenType.DOMAIN_INDEX
    assert tkns[2].type == TokenType.DAILY
    assert tkns[3].type == TokenType.CLOSE
    assert tkns[4].type == TokenType.EOF


def test_scanner_switch_error_catch():
    src = "Close < @"
    scanner = _scn(src)
    tkns = scanner.scan_tokens()
    assert tkns[0].type == TokenType.CLOSE
    assert tkns[1].type == TokenType.LT
    assert tkns[2].type == TokenType.EOF
    _debug_tkns(tkns, False)
    # the '@' char should be caught as an error and added to error list
    assert len(scanner.errors) == 1


def test_scanner_switch_can_recognize_frequency_tokens_weekly_01():
    src = "TWO WEEKS AGO Close"
    scanner = _scn(src)
    tkns = scanner.scan_tokens()
    _debug_tkns(tkns, False)
    assert len(tkns) == 5
    assert tkns[0].type == TokenType.TWO
    assert tkns[1].type == TokenType.DOMAIN_INDEX
    assert tkns[2].type == TokenType.WEEKLY
    assert tkns[3].type == TokenType.CLOSE
    assert tkns[4].type == TokenType.EOF


def test_scanner_switch_can_recognize_frequency_tokens_weekly_02():
    src = "ONE WEEK AGO Close"
    scanner = _scn(src)
    tkns = scanner.scan_tokens()
    _debug_tkns(tkns, False)
    assert len(tkns) == 5
    assert tkns[0].type == TokenType.ONE
    assert tkns[1].type == TokenType.DOMAIN_INDEX
    assert tkns[2].type == TokenType.WEEKLY
    assert tkns[3].type == TokenType.CLOSE
    assert tkns[4].type == TokenType.EOF


def test_scanner_switch_can_recognize_frequency_tokens_monthly_01():
    src = "TWO MONTHS AGO Close"
    scanner = _scn(src)
    tkns = scanner.scan_tokens()
    _debug_tkns(tkns, False)
    assert len(tkns) == 5
    assert tkns[0].type == TokenType.TWO
    assert tkns[1].type == TokenType.DOMAIN_INDEX
    assert tkns[2].type == TokenType.MONTHLY
    assert tkns[3].type == TokenType.CLOSE
    assert tkns[4].type == TokenType.EOF


def test_scanner_switch_can_recognize_frequency_tokens_monthly_01():
    src = "ONE MONTH AGO Close"
    scanner = _scn(src)
    tkns = scanner.scan_tokens()
    _debug_tkns(tkns, False)
    assert len(tkns) == 5
    assert tkns[0].type == TokenType.ONE
    assert tkns[1].type == TokenType.DOMAIN_INDEX
    assert tkns[2].type == TokenType.MONTHLY
    assert tkns[3].type == TokenType.CLOSE
    assert tkns[4].type == TokenType.EOF


def _scn(src: str):
    return StatementScanner(src)


def _tkns(src: str):
    scanner = _scn(src)
    return scanner.scan_tokens()


def _debug_tkns(tkns, bool=True):
    if bool is True:
        print("")
        print("--- DEBUG ----")
        for t in tkns:
            print(t.to_string())
        print("--- END DEBUG ----")
        print("")
