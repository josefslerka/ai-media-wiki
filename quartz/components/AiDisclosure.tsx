import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

// Drobná deklarace AI pod titulkem (procesní, dopředu, s odkazem na plnou deklaraci v /o-projektu).
export default (() => {
  const AiDisclosure: QuartzComponent = ({ displayClass }: QuartzComponentProps) => (
    <p
      class={classNames(displayClass, "ai-disclosure")}
      style="font-size:0.8rem;line-height:1.4;color:var(--gray);border-left:3px solid var(--lightgray);padding-left:0.7rem;margin:0.6rem 0 1.2rem 0;"
    >
      ⓘ Tuto stránku připravil AI agent. Výběr zdrojů, jejich posouzení a odpovědnost jsou lidské; ne
      každá věta prošla individuální redakcí. → <a href="/o-projektu">Jak báze vzniká</a>
    </p>
  )
  return AiDisclosure
}) satisfies QuartzComponentConstructor
