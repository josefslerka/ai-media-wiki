import { QuartzEmitterPlugin } from "../types"
import { write } from "./helpers"
import { FullSlug } from "../../util/path"

// Ověřovací HTML soubor pro Google Search Console (musí být v kořeni domény).
const TOKEN = "googlef21f0aaab18dc769"

export const GoogleSiteVerification: QuartzEmitterPlugin = () => ({
  name: "GoogleSiteVerification",
  async emit(ctx) {
    const path = await write({
      ctx,
      content: `google-site-verification: ${TOKEN}.html`,
      slug: TOKEN as FullSlug,
      ext: ".html",
    })
    return [path]
  },
  async *partialEmit() {},
})
