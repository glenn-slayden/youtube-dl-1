# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class MakerTVIE(InfoExtractor):
    _VALID_URL = r'https?://(?:(?:www\.)?maker\.tv/(?:[^/]+/)?video|http://makerplayer.com/embed/maker)/(?P<id>[a-zA-Z0-9]{12})'
    _TEST = {
        'url': 'http://www.maker.tv/video/Fh3QgymL9gsc',
        'md5': 'ca237a53a8eb20b6dc5bd60564d4ab3e',
        'info_dict': {
            'id': 'brOEcGut',
            'ext': 'mp4',
            'title': 'Maze Runner: The Scorch Trials Official Movie Review',
            'description': 'md5:11ff3362d7ef1d679fdb649f6413975a',
            'upload_date': '20150918',
            'timestamp': 1442549540,
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        jwplatform_id = self._search_regex([r'jwid="([^"]+)"', r'Maker.jw_id\s*=\s*"([^"]+)";'], webpage, 'jwplatform id')

        return self.url_result('jwplatform:%s' % jwplatform_id, 'JWPlatform')
