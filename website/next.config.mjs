import nextra from 'nextra'

const withNextra = nextra({
  theme: 'nextra-theme-docs',
  themeConfig: './theme.config.tsx',
  defaultShowCopyCode: true,
})

export default withNextra({
  output: 'export',
  basePath: process.env.PAGES_BASE_PATH || '',
  images: {
    unoptimized: true,
  },
})
