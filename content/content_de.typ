// Einfache TODO-Blöcke. Alternativ können auch Pakete für Randnotizen genutzt werden.
#let todo(color: orange, body) = {
  box(fill: color, width: 100%, inset: 8pt, radius: 5pt, stroke: black)[#body]
}

= Einleitung
#todo[
  - Einführung in das Thema
  - Motivation des Themas
  - Problemstellung und Forschungsziele
    - (optional) Warum andere Ansätze unzureichend sind / Originalität deiner Arbeit
  - Forschungsfragen und/oder vorgeschlagene (neue) Lösung
  - (optional) Zusammenfassung der Ergebnisse / Resultate der Evaluation
]
== Aufbau dieser Arbeit
#todo[Beschreibe kurz den Aufbau der einzelnen Kapitel]

= Grundlagen

= Analyse
== Verwandte Arbeiten
== Lösungsansatz / Methodik

= Implementierung / Fallstudie

= Ergebnisse / Evaluation

= Diskussion / Kritische Würdigung

= Fazit & Ausblick
