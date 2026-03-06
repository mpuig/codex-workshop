import { useRouter } from 'next/router'
import type { DocsThemeConfig } from 'nextra-theme-docs'

const config: DocsThemeConfig = {
  logo: <strong>OpenAI Codex Workshop</strong>,
  project: {
    link: 'https://github.com/mpuig/codex-workshop',
  },
  docsRepositoryBase: 'https://github.com/mpuig/codex-workshop/tree/main/website',
  feedback: {
    content: 'Give us feedback →',
    useLink: () => 'https://github.com/mpuig/codex-workshop/issues/new?title=Feedback%20for%20%E2%80%9CCodex%20Code%20Workshop%E2%80%9D&labels=feedback',
  },
  darkMode: true,
  color: {
    hue: 169,
    saturation: 60,
  },
  sidebar: {
    defaultMenuCollapseLevel: 1,
  },
  head: function Head() {
    const { asPath } = useRouter()
    const title = asPath === '/'
      ? 'OpenAI Codex Workshop'
      : `OpenAI Codex Workshop`
    return (
      <>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta property="og:title" content={title} />
        <meta property="og:description" content="Practical training for consultancy teams on using OpenAI Codex" />
        <meta property="og:type" content="website" />
      </>
    )
  },
  footer: {
    content: (
      <span>
        OpenAI Codex Workshop &middot; {new Date().getFullYear()}
      </span>
    ),
  },
}

export default config
