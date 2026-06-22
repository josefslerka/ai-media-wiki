import { QuartzEmitterPlugin } from "../types"
import { write } from "./helpers"
import { FullSlug } from "../../util/path"

// Zapíše robots.txt do kořene webu s odkazem na sitemapu (kvůli objevitelnosti / Search Console).
export const RobotsTxt: QuartzEmitterPlugin = () => ({
  name: "RobotsTxt",
  async emit(ctx) {
    const base = ctx.cfg.configuration.baseUrl
    const sitemap = base ? `https://${base}/sitemap.xml` : "/sitemap.xml"
    const content = ["User-agent: *", "Allow: /", "", `Sitemap: ${sitemap}`, ""].join("\n")
    const path = await write({
      ctx,
      content,
      slug: "robots" as FullSlug,
      ext: ".txt",
    })
    return [path]
  },
  async *partialEmit() {},
})
