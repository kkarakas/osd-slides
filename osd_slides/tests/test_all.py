from unittest.mock import patch, call, MagicMock

import pytest
from bs4 import BeautifulSoup
from osd_slides.main import (
    fefmalsmc,
    showDownloadablePdf,
    searchAndDownloadPdf,
    downloadPdf, readAvailableHtmlDocs,
)
import sys
import os


@patch("builtins.print")
def test_main0(mock_print):
    testargs = ["prog", "download", "randomstuff"]
    with patch.object(sys, "argv", testargs):
        fefmalsmc()
        assert mock_print.call_args.args == ("Too many arguments",)


@patch("builtins.print")
def test_main1(mock_print):
    testargs = ["prog"]
    with patch.object(sys, "argv", testargs):
        fefmalsmc()
        assert mock_print.call_args.args == ("Too few arguments",)


# basically mock the function it is calling


def test_main2(mocker):
    mocked_searchAndDownloadPdf = mocker.patch("osd_slides.main.searchAndDownloadPdf")  # noqa: E501

    testargs = ["prog", "download"]
    with patch.object(sys, "argv", testargs):
        fefmalsmc()
        mocked_searchAndDownloadPdf.assert_called_once()


def test_main3(mocker):
    mocked_searchAndDownloadPdf = mocker.patch("osd_slides.main.showDownloadablePdf")  # noqa: E501
    testargs = ["prog", "show"]
    with patch.object(sys, "argv", testargs):
        fefmalsmc()
        mocked_searchAndDownloadPdf.assert_called_once_with()


# TODO one more case where nothing is called


def test_searchAndDownloadPdf(mocker):
    mocked_downloadPdf = mocker.patch("osd_slides.main.downloadPdf")
    data = [
        """<tr><td valign="top"><img alt="[TXT]" src="/icons/text.gif"/>
        </td><td><a href="01-intro.html">01-intro.html</a></td>
        <td align="right">2023-03-04 14:38
        </td><td align="right"> 19K</td><td> </td></tr>""",
        """<tr><td valign="top"><img alt="[TXT]" src="/icons/text.gif"/>
        </td><td><a href="02-history.html">02-history.html</a></td>
        <td align="right">2023-03-04 14:38  </td>
        <td align="right"> 20K</td><td> </td></tr>""",
    ]

    soup = []
    for datum in data:
        soup.append(BeautifulSoup(datum, "html.parser"))
    # TODO repetitive work maybe have a class structure?
    mocker.patch("osd_slides.main.readAvailableHtmlDocs", return_value=soup)
    searchAndDownloadPdf()
    #  check what is download called with assert_called_with
    calls = [call("01-intro.html"), call("02-history.html")]
    mocked_downloadPdf.assert_has_calls(calls)


# TODO unsuccessful test for searchAndDownloadPdf


@patch("builtins.print")
def test_showDownloadablePdf0(mock_print, mocker):
    #  successful read
    data = [
        """<tr><td valign="top"><img alt="[TXT]" src="/icons/text.gif"/></td><td><a href="01-intro.html">01-intro.html</a></td><td align="right">2023-03-04 14:38  </td><td align="right"> 19K</td><td> </td></tr>""",  # noqa: E501
        """<tr><td valign="top"><img alt="[TXT]" src="/icons/text.gif"/></td><td><a href="02-history.html">02-history.html</a></td><td align="right">2023-03-04 14:38  </td><td align="right"> 20K</td><td> </td></tr>""",  # noqa: E501
    ]
    soup = []
    for datum in data:
        soup.append(BeautifulSoup(datum, "html.parser"))

    mocker.patch("osd_slides.main.readAvailableHtmlDocs", return_value=soup)
    showDownloadablePdf()

    assert mock_print.call_args_list[0].args == ("01-intro.html",)
    assert mock_print.call_args_list[1].args == ("02-history.html",)


# TODO unsuccessful test for downloadable


def test_readAvailableHtmlDocs(mocker):
    # TODO work on this
    # make requests.get send a weird
    # make soup have a predetermied value
    text = \
        '''
<html>
<head>
<title>Index of /~paine/4995/lectures</title>
</head>
<body>
<h1>Index of /~paine/4995/lectures</h1>
<table>
<tr><th valign="top"><img alt="[ICO]" src="/icons/blank.gif"/></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr> # noqa: E501
<tr><th colspan="5"><hr/></th></tr>
<tr><td valign="top"><img alt="[PARENTDIR]" src="/icons/back.gif"/></td><td><a href="/~paine/4995/">Parent Directory</a></td><td> </td><td align="right">  - </td><td> </td></tr> # noqa: E501
<tr><td valign="top"><img alt="[TXT]" src="/icons/text.gif"/></td><td><a href="01-intro.html">01-intro.html</a></td><td align="right">2023-03-05 13:21  </td><td align="right"> 19K</td><td> </td></tr> # noqa: E501
<tr><td valign="top"><img alt="[TXT]" src="/icons/text.gif"/></td><td><a href="02-history.html">02-history.html</a></td><td align="right">2023-03-05 13:21  </td><td align="right"> 20K</td><td> </td></tr> # noqa: E501
<tr><td valign="top"><img alt="[TXT]" src="/icons/text.gif"/></td><td><a href="03-git.html">03-git.html</a></td><td align="right">2023-02-14 22:46  </td><td align="right"> 25K</td><td> </td></tr> # noqa: E501
</table>
<address>Apache/2.4.29 (Ubuntu) Server at www.cs.columbia.edu Port 443</address> # noqa: E501
</body></html>'''
    expectedOutput = ['<tr><td valign="top"><img alt="[TXT]" src="/icons/text.gif"/></td><td><a href="01-intro.html">01-intro.html</a></td><td align="right">2023-03-05 13:21  </td><td align="right"> 19K</td><td> </td></tr>',  # noqa: E501
                      '<tr><td valign="top"><img alt="[TXT]" src="/icons/text.gif"/></td><td><a href="02-history.html">02-history.html</a></td><td align="right">2023-03-05 13:21  </td><td align="right"> 20K</td><td> </td></tr>', # noqa: E501
                      '<tr><td valign="top"><img alt="[TXT]" src="/icons/text.gif"/></td><td><a href="03-git.html">03-git.html</a></td><td align="right">2023-02-14 22:46  </td><td align="right"> 25K</td><td> </td></tr>']  # noqa: E501
    soup = MagicMock(text=text)
    # soup["text"] = text
    mocker.patch('requests.get',
                 return_value=soup)
    output = readAvailableHtmlDocs()
    for i in range(len(output)):
        output[i] = str(output[i])
    assert output == expectedOutput

#TODO unvalid URL testing needed


def test_downloadPdf():
    """
    It takes time as it needs to download a file.
    :return:
    """
    file = "01-intro.html"
    if os.path.isfile("./01-intro.pdf"):
        os.remove("./01-intro.pdf")
    downloadPdf(file)
    assert os.path.isfile("./01-intro.pdf")
    os.remove("./01-intro.pdf")


@pytest.mark.integtest
@patch("builtins.print")
def test_print_downloadable_integration(mock_print):
    # mocked_searchAndDownloadPdf =
    # mocker.patch('osd_slides.main.searchAndDownloadPdf')
    testargs = ["prog", "show"]
    #  TODO improve the testing by mocking
    with patch.object(sys, "argv", testargs):
        fefmalsmc()
        assert mock_print.call_args_list[0].args == ("01-intro.html",)
        assert mock_print.call_args_list[1].args == ("02-history.html",)
        assert mock_print.call_args_list[2].args == ("03-git.html",)


# @pytest.mark.integtest
# def test_download_integration():
#     """
#     Takes a long time as it needs to download good amount of files.
#     """
#     testargs = ["prog", "download"]
#     check = [
#         "01-intro.pdf",
#         "./02-history.pdf",
#         "./03-git.pdf",
#         "./03-projects.pdf",
#         "./04-agile-kanban.pdf",
#         "./04-git.pdf",
#         "./04-starting.pdf",
#         "./05-gh-issues-projects.pdf",
#         "./05-starting.pdf",
#         "./05-testing.pdf",
#         "./06-agile-kanban.pdf",
#         "./06-static.pdf",
#         "./06-testing-libraries.pdf",
#         "./07-docs.pdf",
#         "./07-docs2.pdf",
#         "./07-gh-issues-projects.pdf",
#         "./08-examples.pdf",
#         "./08-packaging-part-one.pdf",
#         "./08-release.pdf",
#         "./08-web.pdf",
#         "./09-examples.pdf",
#         "./09-release.pdf",
#         "./09-testing.pdf",
#         "./10-cicd.pdf",
#         "./10-problems.pdf",
#         "./10-static.pdf",
#         "./11-community.pdf",
#         "./11-problems2.pdf",
#         "./11-static.pdf",
#         "./11-testing-libraries.pdf",
#         "./12-econ.pdf",
#         "./12-testing-libraries.pdf",
#         "./13-legal.pdf",
#         "./13-packaging-part-two.pdf",
#         "./14-cicd-setup.pdf",
#         "./14-final.pdf",
#         "./15-release.pdf",
#     ]
#     for doc in check:
#         if os.path.isfile(doc):
#             os.remove(doc)
#
#     with patch.object(sys, "argv", testargs):
#         fefmalsmc()
#
#         for doc in check:
#             assert os.path.isfile(doc)
#             os.remove(doc)
