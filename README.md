# Away928 — Portfolio Site

A minimal, no-framework portfolio landing page linking to three reviewed public open-source projects.

**Public address:** https://away928.github.io/

**Page content:** GitHub avatar and username, a brief *AI × Investment × Research Systems* introduction, and three project cards. GitHub contribution graphs, follower metrics, activity feed, and other account UI do **not** appear on this standalone site.

## Local preview

From the project root:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765/ in a browser.

## Validation

```bash
python3 scripts/check_site.py
```

All HTML, CSS, and the avatar image are local static assets. There are no analytics scripts, cookies, build dependencies, or JavaScript bundles. External links open GitHub repositories or the project's synthetic static demo.

GitHub Pages serves the root of `main`. Changes to this repository affect only this portfolio site, **not** the GitHub account overview page or underlying project repositories.

## Maintenance

The avatar is a snapshot of the publicly visible GitHub profile avatar and can be updated manually. Project descriptions should be kept consistent with their README files and actual release status.

## License

Site markup and styles are licensed under [MIT](LICENSE). The avatar remains the GitHub account holder's profile image and is not offered as a separately licensed asset.
