# ひとり飯ショート 自動収集版

1. GitHubで新規リポジトリを作り、ZIP内のファイルをすべてアップロード（.githubフォルダも含む）。
2. Google Cloud ConsoleでYouTube Data API v3を有効にしてAPIキーを取得。
3. GitHub Settings → Secrets and variables → Actions に YOUTUBE_API_KEY という名前でキーを登録。
4. GitHub Actions → Refresh recipe candidates → Run workflow で初回収集。
5. GitHub Settings → Pages → Deploy from branch → main / root でサイトを公開。
6. Safariでサイトを開き「ホーム画面に追加」。毎日日本時間9時と21時ごろに自動更新（遅延する場合あり）。

検索はYouTube公式API。4分未満の埋め込み可能な動画候補を収集します。1人前、15分以内、500円以内は確認できないため未確認表示にしてください。Shortsであること自体の確実な判別もできません。動画の複製は行いません。Instagram/TikTokの自動収集は未実装です。GitHub Pagesは公開URLです。APIキーは公開ファイルに書かないでください。
